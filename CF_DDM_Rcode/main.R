library(tidyverse)
library(data.table)
library(ggplot2)


source("functions.R")
source("getRaw.R")

# df %>% 
#   filter(respNum2word.corr == 1) %>%  #删除错误试次
#   group_by("姓名") %>% 
#   filter(respTrials.rt <= (mean(respTrials.rt) + 3*sd(respTrials.rt)),
#          respTrials.rt >= (mean(respTrials.rt) - 3*sd(respTrials.rt))) %>% 
#   ungroup() %>% 
#   group_by(participant,
#            gender,
#            transType,
#            ACC) %>% 
#   summarise(RT = mean(respTrials.rt), .groups = "drop") %>% 
#   pivot_wider(names_from = transType,
#               values_from = RT) -> dfcf.wide

df %>% 
  filter((respNum2word.corr == 1)) %>% 
  mutate(transType = as.factor(transType)) %>% 
  ggplot(aes(transType,respNum2word.rt)) +
  geom_boxplot(aes(colour = 姓名)) +
  facet_grid(. ~ 姓名)





