df= read.csv('./R/R_Studio_Basic/dataset/bike.csv')
df_01= aggregate(data= df, temp ~ season, FUN= 'mean')
df_01
y= c(1:20)
plot(y, type = 'l')
