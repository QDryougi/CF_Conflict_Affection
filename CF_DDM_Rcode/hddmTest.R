df.hddm <- AFF_long
df.hddm %>% 
  filter(respFlanker.corr == 1) %>% 
  #filter(SubIndex != 3 & SubIndex != 7) %>% 
  #filter(SubIndex < 13) %>% 
  mutate(response = respAffWord.corr) %>% 
  mutate(subj_idx = SubIndex) %>% 
  mutate(rt = respAffWord.rt/1000) %>% 
  select(subj_idx, congruency, AffValue, response, rt) %>% 
  filter(!is.na(rt)) %>% 
  write.csv(file = 'df.hddm.csv', row.names = FALSE)



