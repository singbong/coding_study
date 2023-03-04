#rbind(), cbind()

df1= data.frame(aa= 1:2,
                bb= c("a", "b"))
df2= data.frame(aa= 1:2,
                bb= c("c", "d"))
df1
df2
rbind(df1, df2)
rbind(df2, df1)

cbind(df1, df2)

df1$"cc" = "kk"
df1

rbind(df1, df2) # col의 갯수가 같지가 않아서 오류남
ncol(df1)
ncol(df2)


rbind(df1[,-3], df2)
rbind(df1[,-1], df2)# colname이 일치하지 않으면 안됌. cbind()는 rowname과 nrow가 일치해야한다.
df1_sub = df1[,-1]
df1_sub
colnames(df1_sub)= c("aa", "bb")
df1_sub
rbind(df1_sub, df2)

#join()   

bike = read.csv('./dataset/bike.csv')
head(bike)

bike_agg_c = aggregate(data= bike,  casual ~ season, FUN = 'mean')

bike_agg_r = aggregate(data= bike,  registered ~ season, FUN = 'mean')

head(bike_agg_c)

head(bike_agg_r)

cbind(bike_agg_c, bike_agg_r) #데이터가 많아지면 권장하지는 않음

library('dplyr')
inner_join(x = bike_agg_c, y = bike_agg_r,
           by= c("season" = "season"))  #bike c 와 r의 시즌을 통합시킨다

left_join(x = bike_agg_c, y = bike_agg_r,
           by= c("season" = "season"))
bike_c = bike_agg_c[-1,]
bike_r = bike_agg_r[-3,]
bike_c
bike_r

inner_join(x = bike_c, y = bike_r,
           by= c("season" = "season"))  #bike c 와 r의 공통 되는 것만 남긴다다

left_join(x = bike_c, y = bike_r,
          by= c("season" = "season"))

#문제 diamonds.csv 데이터를 불러와서 color가 E인 데이터를 뽑아 dia_E에 저장하고 color가 H인 데이터를 뽑아 dia_H에 저장한 
#후 row 기준으로 묶으시오

dia = read.csv('./dataset/diamonds.csv')
head(dia)
dia_E= dia[grep(pattern = 'E',dia$color),]
head(dia_E)
dia_H= dia[grep(pattern = 'H',dia$color),]
head(dia_H)

rbind(dia_E, dia_H)

#문제 bike.csv데이터를 기준으로 시간별 casual의 평균을 계산한 것과 시간별 registered의 평균을 계산한 것을 시간을
#기준으로 inner join 연산을 실시하시오
library('lubridate')
bike = read.csv('./dataset/bike.csv')
head(bike)
bike_sub1 = aggregate(data= bike, casual ~ hour(bike$datetime), FUN = 'mean')
bike_sub2 = aggregate(data= bike, registered ~ hour(bike$datetime), FUN = 'mean')
head(bike_sub1)
head(bike_sub2)
library('dplyr')
inner_join(x= bike_sub1, y= bike_sub2,
           by= c('hour(bike$datetime)'='hour(bike$datetime)'))
