import sklearn as sk
import numpy as np

from data import*
from sklearn.feature_selection import VarianceThreshold

X = np.load(X_MAT_PATH)
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
XMatrixAfterTransformation=sel.fit_transform(X)
print("X matrix with shape {} has been loaded".format(XMatrixAfterTransformation.shape))

np.save('/work/v/vivek4/stage1_clean_bak_X_matrix_after_featureReduction/stage1_clear_bak_X_matrix_afterFR', XMatrixAfterTransformation)

    
