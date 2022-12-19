import pandas
import numpy as np

R"C:\Users\valle\OneDrive\Documents\EP_DE_Aggrin\Statistics\library14_1\4mer_library14_1_preds.csv"
def statistics(inputpath):
	X = np.loadtxt(inputpath, delimiter=",", usecols = 1)
	r1 = np.mean(X)
	r2 = np.median(X)
	maximum = np.max(X)
	minimium = np.min(X)

	print('path:' + inputpath)
	print('mean:' +r1)
	print('median:' +r2)
	print('min:' + minimium)
	print('max:' + maximum)


statistics(R"C:\Users\valle\OneDrive\Documents\EP_DE_Aggrin\Statistics\library14_1\4mer_library14_1_preds.csv")
statistics(R"C:\Users\valle\OneDrive\Documents\EP_DE_Aggrin\Statistics\library14_1\10mer_library14_1_preds.csv")
statistics(R"C:\Users\valle\OneDrive\Documents\EP_DE_Aggrin\Statistics\library14_1\dimer_library14_1_preds.csv")
statistics(R"C:\Users\valle\OneDrive\Documents\EP_DE_Aggrin\Statistics\library14_29\library14_29 10mer.csv")
statistics(R"C:\Users\valle\OneDrive\Documents\EP_DE_Aggrin\Statistics\library14_29\library14_29 fourmer.csv")
statistics(R"C:\Users\valle\OneDrive\Documents\EP_DE_Aggrin\Statistics\library14_29\library14_29_dimer.csv")
