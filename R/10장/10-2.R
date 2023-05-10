noun2 <- unlist(noun)              
wordcount <- table(noun2)         
temp <- sort(wordcount, decreasing=T)[1:10]  p
temp <- temp[-1]    
barplot(temp,
        names.arg = names(temp), ="lightblue",         # ?????? ????󵵼? ??�� ?ܾ?", ylab = "?ܾ? ?󵵼?")