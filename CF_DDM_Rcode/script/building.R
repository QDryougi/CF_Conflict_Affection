AFF_long %>% 
  group_by(SubIndex) %>% 
  dplyr::summarise(age = mean(age), sex = first(sex), .groups = "drop") -> test
mean(test$age)
sd(test$age)

table(test$sex)
