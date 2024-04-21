# 自定义函数

# 合并psychopy数据文件
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

# 计算错误率
errRate <- function(df){
  m <- sum(df == 0)
  1-m/length(df)
}

# 离群值检测（对于每个因变量）
# 输入参数3为变量名
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
    mean_val <- mean(col_data)
    sd_val <- sd(col_data)
    upper_limit <- mean_val + 2.5 * sd_val
    lower_limit <- mean_val - 2.5 * sd_val
    unusuals[[col_name]] <- which(col_data > upper_limit | col_data < lower_limit)
  }
  
  # Combine the results
  result <- list()
  for (i in seq_along(unusuals)) {
    result[[i]] <- data %>% select(!!index) %>% slice(unusuals[[i]])
  }
  names(result) <- sapply(cols, quo_name)
  
  return(result)
}


# 拆分block函数
split_block <- function(m){
  df.block <- AFF_long %>% 
    filter(respFlanker.corr == 1 & respAffWord.corr == 1) %>%
    filter(blocks == m) %>% 
    group_by(SubIndex, congruency, AffValue) %>% 
    filter(respAffWord.rt <= (mean(respAffWord.rt) + 1.96*sd(respAffWord.rt)),
           respAffWord.rt >= (mean(respAffWord.rt) - 1.96*sd(respAffWord.rt))) %>% 
    summarise(Acc.target = mean(Acc.Target), RT.target = mean(respAffWord.rt), .groups = "drop")
  df.block$block <- rep(m, nrow(df.block))
  return(df.block)
}


# 来自互联网
# https://gist.github.com/Karel-Kroeze/746685f5613e01ba820a31e57f87ec87
# 绘制分层提琴图
GeomSplitViolin <- ggproto("GeomSplitViolin", GeomViolin, draw_group = function(self, data, ..., draw_quantiles = NULL){
  data <- transform(data, xminv = x - violinwidth * (x - xmin), xmaxv = x + violinwidth * (xmax - x))
  grp <- data[1,'group']
  newdata <- plyr::arrange(transform(data, x = if(grp%%2==1) xminv else xmaxv), if(grp%%2==1) y else -y)
  newdata <- rbind(newdata[1, ], newdata, newdata[nrow(newdata), ], newdata[1, ])
  newdata[c(1,nrow(newdata)-1,nrow(newdata)), 'x'] <- round(newdata[1, 'x']) 
  if (length(draw_quantiles) > 0 & !scales::zero_range(range(data$y))) {
    stopifnot(all(draw_quantiles >= 0), all(draw_quantiles <= 
                                              1))
    quantiles <- ggplot2:::create_quantile_segment_frame(data, draw_quantiles)
    aesthetics <- data[rep(1, nrow(quantiles)), setdiff(names(data), c("x", "y")), drop = FALSE]
    aesthetics$alpha <- rep(1, nrow(quantiles))
    both <- cbind(quantiles, aesthetics)
    quantile_grob <- GeomPath$draw_panel(both, ...)
    ggplot2:::ggname("geom_split_violin", grid::grobTree(GeomPolygon$draw_panel(newdata, ...), quantile_grob))
  }
  else {
    ggplot2:::ggname("geom_split_violin", GeomPolygon$draw_panel(newdata, ...))
  }
})
geom_split_violin <- function (mapping = NULL, data = NULL, stat = "ydensity", position = "identity", ..., draw_quantiles = NULL, trim = TRUE, scale = "area", na.rm = FALSE, show.legend = NA, inherit.aes = TRUE) {
  layer(data = data, mapping = mapping, stat = stat, geom = GeomSplitViolin, position = position, show.legend = show.legend, inherit.aes = inherit.aes, params = list(trim = trim, scale = scale, draw_quantiles = draw_quantiles, na.rm = na.rm, ...))
}

# http://www.cookbook-r.com/Manipulating_data/Summarizing_data/
# 用于输出描述统计
summarySE <- function(data=NULL, measurevar, groupvars=NULL, na.rm=FALSE,
                      conf.interval=.95, .drop=TRUE) {
  # New version of length which can handle NA's: if na.rm==T, don't count them
  length2 <- function (x, na.rm=FALSE) {
    if (na.rm) sum(!is.na(x))
    else       length(x)
  }
  
  # This does the summary. For each group's data frame, return a vector with
  # N, mean, and sd
  datac <- ddply(data, groupvars, .drop=.drop,
                 .fun = function(xx, col) {
                   c(N    = length2(xx[[col]], na.rm=na.rm),
                     mean = mean   (xx[[col]], na.rm=na.rm),
                     sd   = sd     (xx[[col]], na.rm=na.rm)
                   )
                 },
                 measurevar
  )
  
  # Rename the "mean" column    
  datac <- plyr::rename(datac, c("mean" = measurevar))
  
  datac$se <- datac$sd / sqrt(datac$N)  # Calculate standard error of the mean
  
  # Confidence interval multiplier for standard error
  # Calculate t-statistic for confidence interval: 
  # e.g., if conf.interval is .95, use .975 (above/below), and use df=N-1
  ciMult <- qt(conf.interval/2 + .5, datac$N-1)
  datac$ci <- datac$se * ciMult
  
  return(datac)
}



