source("functions.R")
source("getRaw.R")

#barplot
df %>% 
  filter(respNum2word.corr == 1) %>% 
  mutate(transType = as.factor(transType)) %>% 
  ggplot(aes(transType,respNum2word.rt)) +
  geom_boxplot(aes(colour = name)) +
  facet_grid(. ~ name)

df %>% 
  filter(respFlanker.corr == 1) %>% 
  mutate(congruency = as.factor(congruency)) %>%
  mutate(AffValue = as.factor(AffValue)) %>% 
  ggplot(aes(congruency, respFlanker.rt)) +
  geom_boxplot(aes(colour = name)) +
  facet_grid(. ~ name)

df %>% 
  filter(respFlanker.corr == 1) %>% 
  mutate(congruency = as.factor(congruency)) %>%
  mutate(AffValue = as.factor(AffValue)) %>% 
  ggplot(aes(AffValue, respAffWord.rt)) +
  geom_boxplot(aes(colour = name)) +
  facet_grid(. ~ name)




