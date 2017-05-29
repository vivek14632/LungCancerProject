install.packages('oro.dicom')
library('oro.dicom')

data1<-readDICOMFile(file.choose())
names(data1)

ncol(data1$img)

> nrow(data1$img)
[1] 512
> ncol(data1$img)
[1] 512
> image(data1$img)
> image(data1$img)
