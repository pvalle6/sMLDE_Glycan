"""Script that reads in a list of glycans
and runs them through glycowork on HPC"""
import pandas as pd
import os
import ast
import pickle
import itertools
import pkg_resources

import torch
import glycowork
from glycowork.motif.analysis import *
from glycowork.motif.annotate import *
from glycowork.motif.graph import *
from glycowork.motif.processing import *
from glycowork.motif.query import *
from glycowork.motif.tokenization import *
from glycowork.glycan_data.loader import df_species
from glycowork.glycan_data.loader import lib, motif_list, df_glycan, glycan_binding

import esm
from numpy import loadtxt

lib = get_lib(list(set(df_glycan.glycan.values.tolist() +
                       motif_list.motif.values.tolist() +
                       glycan_binding.columns.values.tolist()[:-2] +
                       ['Monosaccharide'])))
print(lib)
