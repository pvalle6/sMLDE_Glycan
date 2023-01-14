"""Gets the statistics of a csv file
with an index and a single column"""
import numpy as np


def statistics(inputpath):
    x = np.loadtxt(inputpath, delimiter=",", usecols=1)
    r1 = np.mean(x)
    r2 = np.median(x)
    maximum = np.max(x)
    minimium = np.min(x)

    print('path:' + inputpath)
    print('mean:' + str(r1))
    print('median:' + str(r2))
    print('min:' + str(minimium))
    print('max:' + str(maximum))


statistics(R"C:\Users\Hotsauce141\Downloads\Preds\Preds\dimer_mammalian_preds.csv")
statistics(R"C:\Users\Hotsauce141\Downloads\Preds\Preds\tetramer_mammalian_preds.csv")
statistics(R"C:\Users\Hotsauce141\Downloads\Preds\Preds\decamer_mammalian_preds.csv")
statistics(R"C:\Users\Hotsauce141\Downloads\Preds\Preds\twentymer_mammalian_preds.csv")
