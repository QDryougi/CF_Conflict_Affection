dir <- "C:/Users/Ryougi mana/Desktop/CF_DDM/expriment/main/data"

cols <- c("姓名","性别","年龄（周岁）","条件","NumBlock1.thisN","NumBlock2.thisN",
          "respNum2word.corr","respNum2word.rt","congruency","AffValue",
          "AffBlocks.thisN","AffBlock1.thisN","respFlanker.corr","respFlanker.rt",
          "respAffWord.corr","respAffWord.rt")
filters <- c("NumBlock1.thisN","NumBlock2.thisN","AffBlock1.thisN")

df <- mergePy(PATH = dir, COLNAMES = cols, FILTERS = filters) %>% 
  select(-c("NumBlock1.thisN","NumBlock2.thisN")) %>% 
  mutate(respNum2word.rt = respNum2word.rt*1000) %>% 
  mutate(respFlanker.rt = respFlanker.rt*1000) %>% 
  mutate(respAffWord.rt = respAffWord.rt*1000)
colnames(df)[4] <- "transType"