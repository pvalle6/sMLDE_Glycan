import pandas

fileIn = "/ddnA/project/jjung1/pvalle6/preds/sorted/output_sorted.csv"
df = pd.read_csv(fileIn,header = None,index_col=False)

df.plot()
df.plot.scatter(0,1)
plt.savefig('distribution_plot.pdf')