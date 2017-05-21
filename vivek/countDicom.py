# This file is used to count number of DICOM
# files in any folder consisting of patients' folders
# such as stage1 or stage2 or sample_images

# the following code is useful to get the username to identify
# the computer on which the code is running and use the corresponding
# path where we have stored the data
if(getpass.getuser()=='vivek4'):
	dirname='/work/v/vivek4/stage1'
else:
	# please provide your path to data directory	
	print('error: specify directory name for the stage 1')

#total number of dicom files
count=0

# we need to count number of dicom files to create numpy matrix
for directories in os.listdir(dirname):
  files=os.listdir(dirname+'/'+directories+'/')
  count=count+length(files)
  
print('Total number of dcm files='+str(count)  
