# author: vivek

# Purpose: count minimum and maximum pixel value present in each set of dicom images

import preprocessing

if(getpass.getuser()=='vivek4'):
	dirname='/work/v/vivek4/stage1'
else:
	print('error: specify directory name for the stage 1')

#to find min and max in different folders
for directories in os.listdir(dirname):

	ct_scan = read_ct_scan(dirname+'/'+directories+'/')
	segmented_ct_scan = segment_lung_from_ct_scan(ct_scan)
	segmented_ct_scan[segmented_ct_scan < 604] = 0 # not sure if we should do this. I got everything black after I did this transformation

	print('folder name='+directories)
	print('min='+str(np.amin(segmented_ct_scan)))
	print('max='+str(np.amax(segmented_ct_scan)))



