if(getpass.getuser()=='vivek4'):
	dirname='/work/v/vivek4/stage1'
else:
	print('error: specify directory name for the stage 1')

#total number of dicom files
count=0

# we need to count number of dicom files to create numpy matrix
for directories in os.listdir(dirname):
  files=os.listdir(dirname+'/'+directories+'/')
  count=count+length(files)
  
print('Total number of dcm files='+str(count)  
