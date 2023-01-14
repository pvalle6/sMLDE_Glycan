#import pandas as pd
filepath = R"C:\Users\Hotsauce141\Downloads\import.txt"
#glycan_file = pd.read_csv(filepath, header = None)
#glycan_list = glycan_file.values
#print(glycan_list)

from numpy import loadtxt
your_list = []
lines = loadtxt(filepath, dtype=str, comments="#", delimiter=",", unpack=False)


print(lines)