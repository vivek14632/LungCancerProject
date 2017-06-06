import sklearn
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from load_data import*

def convert_df_to_np(df):
    return(np.array(df))

# Get train, test data at the patient level
def get_patient_train_test(file_path):
	os.chdir(file_path)
	files = os.listdir(os.getcwd())
	patient_list = []
	for file in files:
		file_name, file_ext = file.split('.')
		patient_list.append(file_name)
	patients = np.array(patient_list)
	patients_train, patients_test = get_train_test_data(patients)
	print('Number of patients taken as train data : {}'.format(patients_train.shape[0]))
	print('Number of patients taken as test data : {}'.format(patients_test.shape[0]))
	train_x, test_x, train_y, test_y = get_image_train_test(patients_train, patients_test)
	return train_x, test_x, train_y, test_y
	
# Split any numpy into train test sets
def get_train_test_data(np_matrix):
    seed=200
    df = pd.DataFrame(np_matrix)
    train, test = train_test_split(df, test_size = 0.2, random_state=seed)
    train = np.asarray(train)
    test = np.asarray(test)
    return train,test
	
def get_image_train_test(patients_train, patients_test):
    train_df = pd.DataFrame(patients_train, columns=['patient'])
    test_df = pd.DataFrame(patients_test, columns=['patient'])
    Y = np.load(PATIENT_MAT_PATH)
    X = np.load(X_MAT_PATH)
    print('Shape of full X matrix is {}'.format(X.shape))
    print('Shape of full Y matrix is {}'.format(Y.shape))
    df_y = pd.DataFrame(Y, columns=['label', 'patient'])
    df_x = pd.DataFrame(X)
    Y_train = pd.merge(df_y, train_df, on='patient', how='inner')
    Y_test = pd.merge(df_y, test_df, on='patient', how='inner')
    print('Patient Level Y Train data created with shape {}'.format(Y_train.shape))
    print('Patient Level Y Test data created with shape {}'.format(Y_test.shape))
    X_train = df_x.iloc[Y_train.index]
    X_test = df_x.iloc[Y_test.index]
    print('Patient Level X Train data created with shape {}'.format(X_train.shape))
    print('Patient Level X Test data created with shape {}'.format(X_test.shape))
    train_x = convert_df_to_np(X_train)
    train_y = convert_df_to_np(Y_train)
    test_x = convert_df_to_np(X_test)
    test_y = convert_df_to_np(Y_test)
    return train_x, test_x, train_y, test_y
