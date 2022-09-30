import pandas
import matplotlib.pyplot as plt

fileIn = R"C:\Users\valle\Downloads\output_sorted.csv"
#fileIn = "/ddnA/project/jjung1/pvalle6/preds/sorted/output_sorted.csv"
df = pandas.read_csv(fileIn,header = None,index_col=False)

plot = df.plot.hist(column=1,range=[0.1, 1.2],edgecolor='black', bins = 1000)
plt.savefig(R"C:\Users\valle\OneDrive\Documents\EP_DE_Aggrin\Statistics\hist.pdf")