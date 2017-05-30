import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split

def get_train_test_data(np_matrix):
	seed=200
	df = pd.DataFrame(np_matrix)
	train, test = train_test_split(df, test_size = 0.2, random_state=seed)
	return train,test
