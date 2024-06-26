library(xlsx)
df <- read.xlsx(file = "num2word.xlsx", sheetIndex = 1)
colnames(df)[3] <- "条件"

df$target <- sample(df$target)
df.prac <- df[1:20,]
df.prac$truetarget <- ifelse(df.prac$反应类型 == 1,
                        gsub(".*?([a-zA-Z]+).*", "\\1", df.prac$target),
                        as.numeric(gsub(".*?([0-9]+).*", "\\1", df.prac$target)))
df.prac$CorAns <- ifelse(is.na(as.numeric(df.prac$truetarget)), 
                    ifelse(grepl("[A-Z]", df.prac$truetarget), "a", "l"), 
                    ifelse(as.numeric(df.prac$truetarget) %% 2 == 0, "l", "a"))
write.xlsx(df.prac, "practise.xlsx",sheetName = "sheet1")



df$target <- sample(df$target)
df$truetarget <- ifelse(df$反应类型 == 1,
                     gsub(".*?([a-zA-Z]+).*", "\\1", df$target),
                     as.numeric(gsub(".*?([0-9]+).*", "\\1", df$target)))
df$CorAns <- ifelse(is.na(as.numeric(df$truetarget)), 
                                ifelse(grepl("[A-Z]", df$truetarget), "a", "l"), 
                                ifelse(as.numeric(df$truetarget) %% 2 == 0, "l", "a"))
write.xlsx(df, "NumCon.xlsx",sheetName = "sheet1")




