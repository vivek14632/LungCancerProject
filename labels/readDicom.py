import os
import dicom
import numpy

#why are you reading a folder only?
PathDicom = "/home/ravi/sample_images/00cba091fa4ad62cc3200a657aeb957e"


listFilesDCM = []  
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():
            listFilesDCM.append(os.path.join(dirName,filename)) #corrected variable

for i in range(0,len(listFilesDCM)):
	DF = []
	DF[i] = dicom.read_file(listFilesDCM[0])
	
	ConstPixelDims[i] = (int(DF[i].Rows), int(DF[i].Columns), len(listFilesDCM))
	ConstPixelSpacing[i] = (float(DF[i].ConstPixelSpacing[0]), float(DF[i].ConstPixelSpacing[1]))
	
	
x = numpy.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
y = numpy.arange(0.0, (ConstPixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])

print(x)
print(y)

ArrayDicom = numpy.zeros(ConstPixelDims, dtype=DF.pixel_array.dtype)


for filenameDCM in listFilesDCM:
    # read the file
    ds = dicom.read_file(filenameDCM)
    # store the raw image data
    ArrayDicom[:, :, listFilesDCM.index(filenameDCM)] = ds.pixel_array

	
print(ArrayDicom)

