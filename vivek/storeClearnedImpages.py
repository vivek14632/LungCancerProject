# author: vivek

# Purpose: This file is used to clear the dicom image and store as numpy objects

import os
from  preprocessing import * 
from  NumpyMatrix import *

INPUT_FOLDER='/work/v/vivek4/stage1'
DESTINATION_FOLDER='/work/v/vivek4/stage1_clean'

# we need to count number of dicom files to create numpy matrix
for directories in os.listdir(INPUT_FOLDER):
	ct_scan=read_ct_scan(INPUT_FOLDER+'/'+directories+'/')
	temp=segment_lung_from_ct_scan(ct_scan)
	saveNumpy(temp,DESTINATION_FOLDER+'/'+directories)


