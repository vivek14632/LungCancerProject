# authors: vivek
# To know how many in the Y variable are 0 and how may are 1 to
# determine the baseline for a random coin toss

import numpy as np
from data import * 
from load_data import *
X,Y = load_data()
print('Number of 1 in Y ='+str(sum(Y)))
print('Total number of samples='+str(Y.shape[0]))
print('Percenttage of 1s ='+str(sum(Y)/float(Y.shape[0])))