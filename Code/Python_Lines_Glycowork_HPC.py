#pip uninstall torch-scatter --yes 
#pip uninstall torch-sparse --yes
#pip uninstall torch-cluster --yes
#pip uninstall torch-spline-conv --yes
#pip uninstall torch-geometric --yes
#pip uninstall glycowork --y

#pip install torch-scatter -f https://data.pyg.org/whl/torch-1.12.0+cu102.html
#pip install torch-sparse --no-cache-dir -f https://data.pyg.org/whl/torch-1.12.0+cu102.html
#pip install torch-cluster -f https://data.pyg.org/whl/torch-1.12.0+cu102.html
####pip install torch-spline-conv -f https://data.pyg.org/whl/torch-1.12.0+cu102.html
#pip install torch-geometric -f https://data.pyg.org/whl/torch-1.12.0+cu102.html
#pip install glycowork


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

#!pip install nbdev

#import warnings
#warnings.filterwarnings("ignore")
#from nbdev.showdoc import show_doc
#from IPython.display import HTML
#%load_ext autoreload
#%autoreload 2

#doesn't work remove later 9/22/22
#os.environ['TORCH_HOME'] = '/ddnA/work/pvalle6/torch'

#!pip install fair-esm
import esm

#below is only needed once to download model 
torch.hub.set_dir('/ddnA/project/jjung1/pvalle6/')
model_esm, alphabet = esm.pretrained.esm1b_t33_650M_UR50S()

#model, alphabet = torch.hub.load("/ddnA/project/jjung1/pvalle6/checkpoints", "esm1b_t33_650M_UR50S", source ='local')

##### PROGRAM #####

#UPDATE TO HPC

filepath = "/home/pvalle6/Chimeras.output"	
file_input = pd.read_csv(filepath, nrows = 100, header = None)
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

nameDF = outprint_multi_protein['name']
splitDF = outprint_multi_protein.preds.str.split(expand = True)
splitDF = splitDF.drop([0,2,3,4,5], axis = 1)
concatDF = pd.concat([nameDF, splitDF], ignore_index=True, sort=False, axis = 1)
#concatDF

concatDF.to_csv("/work/pvalle6/output.csv",header=False, index = False)

####