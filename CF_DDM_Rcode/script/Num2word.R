CF_long <- df[-seq(1,length(df$SubIndex),80),] %>%
  filter(respNum2word.corr >= 0) %>% 
  select(c(SubIndex, transType,respNum2word.corr,respNum2word.rt))



CF_long <- aggregate(CF_long$respNum2word.corr, by=list(SubIndex = CF_long$SubIndex, transType = CF_long$transType),errRate) %>% 
  merge(CF_long, by = c("SubIndex", "transType"),all.x = TRUE)
colnames(CF_long)[3] = 'Accuracy'

CF_long %>% 
  filter(respNum2word.corr == 1) %>%  #删除错误试次
  group_by(SubIndex, transType) %>% 
  filter(respNum2word.rt <= (mean(respNum2word.rt) + 1.96*sd(respNum2word.rt)),
          respNum2word.rt >= (mean(respNum2word.rt) - 1.96*sd(respNum2word.rt))) %>% 
  summarise(Accuracy = mean(Accuracy), Num2word.rt = mean(respNum2word.rt), .groups = "drop") %>%
  pivot_wider(names_from = transType,
              values_from = c(Num2word.rt,Accuracy)) -> CF_wide
colnames(CF_wide)[2:5] <- c("RT.Trans","RT.Repeat",'ACC.Trans','ACC.Repeat')
CF_wide <- mutate(CF_wide, switch_cost = RT.Trans - RT.Repeat)
