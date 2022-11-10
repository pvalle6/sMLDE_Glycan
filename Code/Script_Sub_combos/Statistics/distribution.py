import pandas
import matplotlib.pyplot as plt
fileIn = R"C:\Users\valle\Downloads\output_sorted.csv"
#fileIn = "/ddnA/project/jjung1/pvalle6/preds/sorted/output_sorted.csv"
df = pandas.read_csv(fileIn,header = None,index_col=False)

plot = df.plot.line(y=1)
plt.savefig('dis.pdf')