import dicom
import os
import pandas as pd
import numpy as np


def print_final_matrix (data_dir):
    destination_dir = '/home/ravi/'
    data_dir = '/home/cis1024/sample_images_clean/'
    patients = os.listdir(data_dir)
    
    #count total number of slices
    total_slices = 0
    for patient in patients[:]:
        mat = np.load(data_dir + patient)
        total_slices += len(mat)
    
    #define final freq matrix
    final_matrix = np.zeros(total_slices*4096, dtype = int).reshape(total_slices,4096)
    #print final_matrix
    
    for patient in patients[:]:
        mat_new = np.load(data_dir + patient)
        for each in len(mat_new):
            
            #go to each slice and get frequency matrix
            x = mat_new[each]
            unique, counts = np.unique(x, return_counts=True)
            freq_mat= np.asarray((unique, counts)).T    
            #update final matrix numpy array
            for j in range(len(freq_mat)):
                final_matrix[each][freq_mat[j][0]] = freq_mat[j][1]
    
    #save matrix
    np.save(destination_dir + 'final_matrix',final_matrix)
