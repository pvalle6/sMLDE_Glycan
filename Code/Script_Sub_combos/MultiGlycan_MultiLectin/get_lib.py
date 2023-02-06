"""Script that reads in a list of glycans
and runs them through glycowork on HPC"""
import pandas as pd
import torch
import glycowork
from glycowork.glycan_data.loader import *
from glycowork.glycan_data.data_entry import *

import esm
from numpy import loadtxt


print("\nLib:")
print(get_lib(df_glycan.glycan.values.tolist()))