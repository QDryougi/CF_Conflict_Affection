source("Num2word.R")
source("AFF.R")

filled_outers1 <- lapply(outers1, function(df) {
  n_missing_rows <- 10 - nrow(df)
  if (n_missing_rows > 0) {
    missing_rows <- data.frame(SubIndex = rep(0, n_missing_rows))
    df <- rbind(df, missing_rows)
  }
  return(df)
})

filled_outers1 <- bind_cols(filled_outers1)
colnames(filled_outers1) <- names(outers1)

filled_outers2 <- lapply(outers2, function(df) {
  n_missing_rows <- 10 - nrow(df)
  if (n_missing_rows > 0) {
    missing_rows <- data.frame(SubIndex = rep(0, n_missing_rows))
    df <- rbind(df, missing_rows)
  }
  return(df)
})

filled_outers2 <- bind_cols(filled_outers2)
colnames(filled_outers2) <- names(outers2)

outers <- cbind(filled_outers1, filled_outers2)

sums <- colSums(outers)
non_zero_cols <- names(outers)[sums != 0]
outers <- outers[, non_zero_cols, drop = FALSE]

AFF_long_Sim <- filter(AFF_long, !(SubIndex %in% OUTERS))




SimpleTest.frame <- merge(CF_wide, AFF_wide, by = 'SubIndex') %>%
  filter(!(SubIndex %in% OUTERS)) %>% 
  select(-c(RT.Trans, RT.Repeat, ACC.Trans, ACC.Repeat))

hist(SimpleTest.frame$Conflict_pos)
hist(SimpleTest.frame$Conflict_neg)

plot(SimpleTest.frame$switch_cost, SimpleTest.frame$Conflict_pos)
plot(SimpleTest.frame$switch_cost, SimpleTest.frame$Conflict_neg)

cor.test(SimpleTest.frame$switch_cost, SimpleTest.frame$Conflict_pos)
cor.test(SimpleTest.frame$switch_cost, SimpleTest.frame$Conflict_neg)

# 假设1：转换代价与情绪词判断-简单反应时正相关
Hypo_1 <- AFF_long_Sim %>% 
  filter(respAffWord.corr == 1 & respFlanker.corr == 1) %>% 
  group_by(SubIndex) %>% 
  summarise(meanRT.G = mean(respAffWord.rt), .groups = 'drop') %>% 
  cbind(SimpleTest.frame$switch_cost) %>% 
  mutate(RT.G = meanRT.G - SimpleTest.frame$RT.prime_Co)

Hypo_1 <- AFF_long_Sim %>% 
  filter(respAffWord.corr == 1 & respFlanker.corr == 1) %>% 
  group_by(SubIndex, AffValue) %>% 
  summarise(meanRT = mean(respAffWord.rt), .groups = 'drop') %>% 
  pivot_wider(names_from = AffValue, values_from = meanRT) %>% 
  cbind(SimpleTest.frame$switch_cost) %>% 
  mutate(RT.pos = pos - SimpleTest.frame$RT.prime_Co, RT.neg = neg - SimpleTest.frame$RT.prime_Co) %>% 
  merge(Hypo_1, by = c('SubIndex', 'SimpleTest.frame$switch_cost'), all.x = TRUE)

cor.test(Hypo_1$`SimpleTest.frame$switch_cost`, Hypo_1$RT.G)
cor.test(Hypo_1$`SimpleTest.frame$switch_cost`, Hypo_1$RT.pos)
cor.test(Hypo_1$`SimpleTest.frame$switch_cost`, Hypo_1$RT.neg)

library(bruceR)
# 分析基础数据
AFF_long_Sim %>% 
  filter(respAffWord.corr == 1 & respFlanker.corr == 1) %>% 
  group_by(SubIndex, congruency, AffValue) %>% 
  summarise(RT = mean(respAffWord.rt)) %>% 
  ggplot(aes(congruency, RT)) +
  geom_boxplot(aes(colour =  as.factor(AffValue)))

RESULT <- AFF_long_Sim %>% 
  filter(respAffWord.corr == 1 & respFlanker.corr == 1) %>%
  MANOVA(subID = 'SubIndex' ,within = c('congruency', 'AffValue'), dv = 'respAffWord.rt') %>% 
  EMMEANS("AffValue", by = "congruency")

