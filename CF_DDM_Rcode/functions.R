mergePy <- function(PATH, COLNAMES, FILTERS) {
  #用于psychopy数据合并
  # packages: tidyverse/data.table
  #输入文件路径，注意用“/” 
  dir <-  PATH
  #输入需要提取的列名
  colName = COLNAMES
  
  #合并后的文件名
  store_csv <- "merged.csv"
  # store_csv <- paste(dir, "merged.csv")
  file.remove(store_csv)
  
  #数据合并
  fileList <- list.files(path = dir, pattern = "*.csv$", 
                         recursive = TRUE, full.names = TRUE)
  
  for (i in 1:length(fileList)) {
    fread(file = fileList[i]) %>% 
      select(colName) %>%
      write_csv(file = store_csv,append = TRUE, col_names = FALSE)
  }
  rowData = read.csv(store_csv)
  colnames(rowData)[] <- colName
  
  # 依据列值进行行删除，如果FILTERS中至少有一列不为NA，则保留行，推荐使用"xxx.thisN"
  rowData <- filter(rowData, rowSums(!is.na(rowData[, FILTERS])) > 0)
  
  return(rowData)
}





