import torch
import glycowork
from glycowork.ml.model_training import *
from glycowork.ml.models import *
from glycowork.ml.processing import *
from glycowork.ml.inference import *
from glycowork.ml.train_test_split import *
from glycowork.ml import models
from glycowork.ml import model_training
#export
from glycowork.glycan_data.loader import *
from glycowork.glycan_data.data_entry import *
#from glycowork.motif.analysis import plot_embeddings, make_heatmap, characterize_monosaccharide, get_pvals_motifs

#!pip install fair-esm
import esm

torch.hub.set_dir('/ddnA/project/jjung1/pvalle6/')
model_esm, alphabet = esm.pretrained.esm1b_t33_650M_UR50S()

#model, alphabet = torch.hub.load("/ddnA/project/jjung1/pvalle6/checkpoints", "esm1b_t33_650M_UR50S", source ='local')

##### PROGRAM #####

maxRow = 4700000
rowSkip = 0
nrowsCount = 2000
filepath = "/home/pvalle6/Chimeras.output"	


#possible make this a function
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
    glycan = ['GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl']

    #multiple protein, single glycan prediction getter
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

    sortedConcatDF = concatDF.sort_values(concatDF.columns[1])
    #rangeDF = concatDF[concatDF.columns[1]]

    #maximum = rangeDF.max(axis=0)
    #minimum = rangeDF.min(axis=0)

    #outRange = (f"/ddnA/project/jjung1/pvalle6/preds/range/range.txt")
    #text_file = open(outRange, "a")
    #text_file.write(maximum)
    #text_file.write('\n')
    #text_file.write(minimum)
    #text_file.close()

    
    
    outPreds = (f"/ddnA/project/jjung1/pvalle6/preds/sorted/output_sorted.csv")
    sortedConcatDF.to_csv(outPreds,mode = 'a',header=False, index = False)


    ####