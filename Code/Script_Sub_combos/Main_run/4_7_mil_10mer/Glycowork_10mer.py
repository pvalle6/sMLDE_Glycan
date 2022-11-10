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

#length of the chimera file rows
maxRow = 4782969
#initial row skip is 0 due to starting at 1
#adjust for continuation of previous job
rowSkip = 0
# memory excedes past 3000 per run
nrowsCount = 2000
filepath = "/ddnA/project/jjung1/pvalle6/chimeras.output"	

#possibly make this a function
#if continuing previous job, adjust row skip 
#split into 2000 iterations to allow garbage collection 
while((rowSkip - nrowsCount) < maxRow):
    file_input = pd.read_csv(filepath, skiprows = rowSkip, nrows = nrowsCount, header = None)
    #iterates the while loop
    rowSkip = rowSkip + nrowsCount

    file_input.columns = ['input']
    file_input = file_input.input.str.split(expand = True)
    proteinNameSeq = file_input.drop([1,2], axis = 1)
    proteinNameSeq.columns = ['NCR', 'SEQUENCE']
    protein_embeddings = []

    protein_seq = proteinNameSeq['SEQUENCE'].tolist()
    protein_dict = get_esm1b_representations(protein_seq, model_esm, alphabet)

    model = prep_model('LectinOracle',1,trained=True)
    outprint_multi_protein = pd.DataFrame(columns = ['name', 'preds'])
    # original glycan
    #glycan = ['GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl']#dimer 
    #glycan = ['GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl'] #four-mer
    glycan = ['GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl'] #ten-mer

    #multiple protein, single glycan prediction getter
    # calls the list of proteins with their embedding pairs and a selected glycan
    a=0
    for index, rows in proteinNameSeq.iterrows():
        outprint_multi_protein.at[a, 'name'] = rows['NCR'] # replace with the actual name when reading from a file
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
    outPreds = (f"/ddnA/project/jjung1/pvalle6/preds/sorted/4_7_mil_10mer.csv")
    concatDF.to_csv(outPreds,mode = 'a',header=False, index = False)


    ####