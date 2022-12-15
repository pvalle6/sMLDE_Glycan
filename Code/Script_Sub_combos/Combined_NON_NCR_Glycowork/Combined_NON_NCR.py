import torch
import glycowork
from glycowork.ml.model_training import *
from glycowork.ml.models import *
from glycowork.ml.processing import *
from glycowork.ml.inference import *
from glycowork.ml.train_test_split import *
from glycowork.ml import models
from glycowork.ml import model_training
from glycowork.glycan_data.loader import *
from glycowork.glycan_data.data_entry import *

import esm

torch.hub.set_dir('/ddnA/project/jjung1/pvalle6/')
#it appears that this function checks for local aswell, don't believe its redownloading 
model_esm, alphabet = esm.pretrained.esm1b_t33_650M_UR50S()
#pure local model call
#model, alphabet = torch.hub.load("/ddnA/project/jjung1/pvalle6/checkpoints", "esm1b_t33_650M_UR50S", source ='local')

##### PROGRAM #####
dimer = ['GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl']
tetramer = ['GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl']
decamer = ['GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl']
twentymer = ['GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)'] 
lectin = "/ddnA/project/jjung1/pvalle6/mammalian_lectins.csv" 

def run_glycowork(lectin_doc, glycan):
    filepath = lectin_doc
    rowSkip = 0
    maxRow = 34
    nrowsCount = 0
    #possibly make this a function
    #if continuing previous job, adjust row skip 
    #split into 2000 iterations to allow garbage collection 
    while((rowSkip - nrowsCount) < maxRow):
        file_input = pd.read_csv(filepath, header = None)
        file_input.columns = ['UNI', 'SEQUENCE']
        
        protein_seq = file_input['SEQUENCE'].tolist()
        protein_dict = get_esm1b_representations(protein_seq, model_esm, alphabet)

        model = prep_model('LectinOracle',1,trained=True)
        outprint_multi_protein = pd.DataFrame(columns = ['name', 'preds'])
        # original glycan
        #multiple protein, single glycan prediction getter
        # calls the list of proteins with their embedding pairs and a selected glycan
        a=0
        for index, rows in file_input.iterrows():
            outprint_multi_protein.at[a, 'name'] = rows['UNI'] # replace with the actual name when reading from a file
            #[pred] is at the end because get_lec returns an array and we only need the pred value
            outprint_multi_protein.at[a, 'preds'] = str((get_lectin_preds((rows['SEQUENCE']), glycan,model,protein_dict))['pred'])
            a +=1

        # recombines individual predictions and removes unnecessary formatting s
        nameDF = outprint_multi_protein['name']
        splitDF = outprint_multi_protein.preds.str.split(expand = True)
        splitDF = splitDF.drop([0,2,3,4,5], axis = 1)
        concatDF = pd.concat([nameDF, splitDF], ignore_index=True, sort=False, axis = 1)

        #sortedConcatDF = concatDF.sort_values(concatDF.columns[1])
        # prediction file appended below
        if glycan == dimer:
            outPreds = (f"/ddnA/project/jjung1/pvalle6/preds/mammalian_lectin_preds/dimer_mammalian_preds.csv")
        if glycan == tetramer:
            outPreds = (f"/ddnA/project/jjung1/pvalle6/preds/mammalian_lectin_preds/tetramer_mammalian_preds.csv")
        if glycan == decamer:
            outPreds = (f"/ddnA/project/jjung1/pvalle6/preds/mammalian_lectin_preds/decamer_mammalian_preds.csv")
        if glycan == twentymer:
            outPreds = (f"/ddnA/project/jjung1/pvalle6/preds/mammalian_lectin_preds/twentymer_mammalian_preds.csv")
        concatDF.to_csv(outPreds,mode = 'a',header=False, index = False)
    ####

run_glycowork(lectin, dimer)
run_glycowork(lectin, tetramer)
run_glycowork(lectin, decamer)
run_glycowork(lectin, twentymer)