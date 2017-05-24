import os
import numpy as np

my_path = r'fully qualified path containing all npy files'
os.chdir(my_path)

# function to get label of each patient
def get_label(x):
    fp=open(r'path containing lable.csv file')
    m_data=fp.readlines()[1:]
    fp.close()
    for m_row in m_data:
        m_row=m_row.split('\n')[0]
        m_row=m_row.split(',')
        if(m_row[0]==x):
            return m_row[1]
        
# function to calculate number of images in each patient file.
def get_tot_images(file): 
    npy_file = np.load(file)
    dim = npy_file.shape
    return(dim[0])

def main():
    # Get all files in current working directory
    files = os.listdir(os.getcwd())
    
    num_imgs = []
    labels = []
    # create a list containing the number of images in each patient file.
    for file in files:
        num_imgs.append(get_tot_images(file))
    
    # create a list that contains the label(0 or 1) repeated n number of times (for each patient) 
    # where n is the number of images for each patient.
    for file, num in zip(files, num_imgs):    
        file_name, file_ext = file.split('.')
        labels.append(get_label(file_name)*num)
    y_ndarray = np.asarray(labels)  
    
if __name__ == '__main__':
    main()
