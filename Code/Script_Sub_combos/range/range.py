import pandas

fileIn = "/ddnA/project/jjung1/pvalle6/preds/sorted/output_sorted.csv"
df = pd.read_csv(fileIn ,header = None,index_col=False)
minVal = df.min()
maxVal = df.max()

with open('/ddnA/project/jjung1/pvalle6/preds/sorted/rangeOut.txt', 'w') as file:
	file.write('min:' + minVal)
	file.write('max:' + maxVal)
