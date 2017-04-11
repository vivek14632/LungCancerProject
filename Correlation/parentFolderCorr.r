
parentFolderCorr <- function(arg1){
  folders  <- list.files(path="C:/Users/gaura/OneDrive - University of South Florida/Gaurav/Projects/Data Science Bowl 2017 - Lung Cancer/Data/sample_images",
                         ,full.names=T)
                         
  for(subFolder in folders){

    fileList <- list.files(subFolder, pattern = "*.dcm", all.files = FALSE, full.names = TRUE)
    
    totalFiles <- length(fileList)
    print(totalFiles)
    z <- 0
    totalCorr <- 0
    
    for(i in 1:(totalFiles-1)) {
        
        for(j in c((i+1):totalFiles)) {
        z <- z + 1
        
        #print(i)
        #print(j)
        #print('')
        data1<-readDICOM(fileList[i])
        #print(fileList[i])
        
        data2<-readDICOM(fileList[j])
        #print(fileList[j])
        
        singleCorr = cor(as.vector(data1$img[[1]]),as.vector(data2$img[[1]]))
        #print(singleCorr)
        totalCorr <- singleCorr + totalCorr
        
        }
    }  
  
  }                        

  
  #return(cor(as.vector(data1$img[[1]]),as.vector(data2$img[[1]])))

  return(totalCorr/z)
  
}

parentFolderCorr("C:/Users/gaura/OneDrive - University of South Florida/Gaurav/Projects/Data Science Bowl 2017 - Lung Cancer/Data/sample_images")
