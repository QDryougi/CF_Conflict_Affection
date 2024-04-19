AFF_long <- df %>%
  filter(respFlanker.corr >= 0) %>%
  select(c(SubIndex, sex, age, AffBlocks.thisN, AffBlock1.thisN ,congruency, 
           AffValue, respFlanker.corr, respFlanker.rt, respAffWord.corr, respAffWord.rt))
colnames(AFF_long)[4:5] <- c('blocks','trails')

AFF_long <- aggregate(AFF_long$respAffWord.corr, by=list(SubIndex = AFF_long$SubIndex,
                                                         congruency = AFF_long$congruency,
                                                         AffValue = AFF_long$AffValue), errRate) %>% 
  merge(AFF_long, by = c("SubIndex", 'congruency', 'AffValue'), all.x = TRUE)  #计算错误率
colnames(AFF_long)[4] = 'Acc.Target'

AFF_long <- aggregate(AFF_long$respFlanker.corr, by=list(SubIndex = AFF_long$SubIndex,
                                                         congruency = AFF_long$congruency), errRate) %>% 
  merge(AFF_long, by = c("SubIndex", 'congruency'), all.x = TRUE)
colnames(AFF_long)[3] = 'Acc.prime'

AFF_long$congruency[AFF_long$congruency == 0] <- 'Co'
AFF_long$congruency[AFF_long$congruency == 1] <- 'Ic'
AFF_long$AffValue[AFF_long$AffValue == 0] <- 'neg'
AFF_long$AffValue[AFF_long$AffValue == 1] <- 'pos'

# 计算冲突积极性（传统方式：RT/ACC体系）
Aff_wide_prime <- AFF_long %>% 
  filter(respFlanker.corr == 1) %>% 
  group_by(SubIndex, congruency) %>% 
  filter(respFlanker.rt <= (mean(respFlanker.rt) + 1.96*sd(respFlanker.rt)),
         respFlanker.rt >= (mean(respFlanker.rt) - 1.96*sd(respFlanker.rt))) %>% 
  ungroup() %>% 
  group_by(SubIndex, congruency) %>% 
  summarise(Acc.prime = mean(Acc.prime), RT.prime = mean(respFlanker.rt), .groups = 'drop') %>% 
  pivot_wider(names_from = c(congruency),
              values_from = c(Acc.prime, RT.prime))

Aff_wide_target <- AFF_long %>% 
  filter(respFlanker.corr == 1 & respAffWord.corr == 1) %>%
  group_by(SubIndex, congruency, AffValue) %>% 
  filter(respAffWord.rt <= (mean(respAffWord.rt) + 1.96*sd(respAffWord.rt)),
         respAffWord.rt >= (mean(respAffWord.rt) - 1.96*sd(respAffWord.rt))) %>% 
  summarise(Acc.target = mean(Acc.Target), RT.target = mean(respAffWord.rt), .groups = "drop") %>% 
  pivot_wider(names_from = c(congruency, AffValue),
              values_from = c(Acc.target, RT.target))

Aff_wide_target$Conflict_pos <- Aff_wide_target$RT.target_Ic_pos - Aff_wide_target$RT.target_Co_pos
Aff_wide_target$Ic_prime_grade <- Aff_wide_target$RT.target_Ic_neg - Aff_wide_target$RT.target_Ic_pos

AFF_wide <- merge(Aff_wide_prime, Aff_wide_target, by = 'SubIndex')

outers2 <- OuterDetectV(AFF_wide, SubIndex, c(14,15))




