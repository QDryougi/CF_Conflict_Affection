library(tidyverse)
library(data.table)
library(ggplot2)


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

errRate <- function(df){
  m <- sum(df == 0)
  1-m/length(df)
}

OuterDetectN <- function(data, index, ...) {
  index <- enquo(index)
  cols <- enquos(...)
  
  unusuals <- list()
  for (col in cols) {
    col_name <- quo_name(col)
    if (!(quo_name(col) %in% names(data))) {
      warning(paste("Column", quo_name(col), "not found in the data frame. Skipping..."))
      next
    }
    col_data <- data[[quo_name(col)]]
    unusuals[[col_name]] <- which(col_data %in% boxplot.stats(col_data)$out)
  }
  
  # Combine the results
  result <- list()
  for (i in seq_along(unusuals)) {
    result[[i]] <- data %>% select(!!index) %>% slice(unusuals[[i]])
  }
  names(result) <- sapply(cols, quo_name)
  
  return(result)
}


OuterDetectV <- function(data, index, ...) {
  index <- enquo(index)
  cols <- list(...)
  
  if(length(cols) == 1 && length(cols[[1]]) == 2 && all(sapply(cols[[1]], is.numeric))) {
    col_range <- as.numeric(cols[[1]])
    cols <- names(data)[col_range[1]:col_range[2]]
  } else {
    cols <- unlist(cols)
  }
  
  unusuals <- list()
  for (col in cols) {
    if (!(col %in% names(data))) {
      warning(paste("Column", col, "not found in the data frame. Skipping..."))
      next
    }
    col_data <- data[[col]]
    unusuals[[col]] <- which(col_data %in% boxplot.stats(col_data)$out)
  }
  
  # Combine the results
  result <- list()
  for (i in seq_along(unusuals)) {
    result[[i]] <- data %>% select(!!index) %>% slice(unusuals[[i]])
  }
  names(result) <- cols
  
  return(result)
}




