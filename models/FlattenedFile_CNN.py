import numpy as np
import os

#data_dir = "C:/Users/maruv/Downloads/sample_images_clean/"

def def_main_matrix(data_dir):
    #define total slices
    total_slices = 0
    
    #define the patients directory
    patients = os.listdir(data_dir)
    
    #calculate complete slices for given set of patients
    for patient in patients[:]:
        mat = np.load(data_dir + patient)
        total_slices += len(mat)
    
    #define new matrix
    new_mat = new = np.ndarray(total_slices*1, dtype = object)
    return new_mat
    
   

def create_flat_mat(matrix):
    new_counter = 0
    for patient in patients[:]:
        patient = np.load(data_dir + patient)
        
        #flatten matrix
        for i in range(len(patient)):
            matrix[new_counter] = patient[i].ravel()
            new_counter += 1
    return matrix
