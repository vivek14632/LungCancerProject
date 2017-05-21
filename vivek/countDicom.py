# This file is used to count number of DICOM
# files in any folder consisting of patients' folders
# such as stage1 or stage2 or sample_images

# the following code is useful to get the username to identify
# the computer on which the code is running and use the corresponding
# path where we have stored the data

import os

def countDicomInaFolder(folderName):
	#total number of dicom files
	count=0
	# we need to count number of dicom files to create numpy matrix
	for directories in os.listdir(folderName):
		files=os.listdir(folderName+'/'+directories+'/')
		count=count+len(files)
	print('Total number of dcm files='+str(count))
	return count 

# test code
if __name__ == '__main__':
	print(str(countDicomInaFolder('/work/v/vivek4/sample_images')))
