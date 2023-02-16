"""Script that reads in a list of glycans
and runs them through glycowork on HPC"""
import pandas as pd
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
from numpy import loadtxt
torch.hub.set_dir('/ddnA/project/jjung1/pvalle6/')
model_esm, alphabet = esm.pretrained.esm1b_t33_650M_UR50S()


#prediction_file = '/ddnA/project/jjung1/pvalle6/preds.csv'
#lines = loadtxt(filepath, dtype=str, unpack=False)

prot_seq = [LG1, LG2, LG3, LG4, LG5,LG1+EGF1, LG2+EGF2, LG1+EGF1+LG2+EGF2+LG3, LG4+EGF3+LG5]
count=0

expansion = '(b1-4)RibOP-ol(5-1)RibOP-ol(5-3)GalNAc(b1-3)GlcNAc(b1-4)Man'
repeat = 'GlcA(b1-3)Xyl(a1-3)'
base = 'GlcA(b1-4)Xyl'
units_add = ''
glycans = []
for i in range(10):
	units_add = ''
	for y in range(i):
		units_add = units_add + repeat
	glycans.append(units_add + base)

for proteins in prot_seq:
	protein_emb_dic = get_esm1b_representations([proteins], model_esm, alphabet)

	leor = prep_model('LectinOracle', 1, trained=True)
	preds = get_lectin_preds(proteins, glycans, leor, protein_emb_dic)
	count = count +1
	preds.to_csv('/ddnA/project/jjung1/pvalle6/preds{0}.csv'.format(count), mode='a', header=False, index=False)
	#
