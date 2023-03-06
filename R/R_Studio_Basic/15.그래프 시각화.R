#01plot() , hist() 기본 내장
plot(1:10)


set.seed(123)
num= sample(1:10, size=10)
num

plot(num, type= 'l') # 타입 l은 선그래프
?plot()

plot(num, type= 'b', col= 'red')

df= iris
head(iris)
plot(df$Sepal.Length, df$Sepal.Width)
hist(df$Sepal.Length) #히스토 그램


#02 ggplot2 패키지

#쉽고 직관적인 문법
#통꼐적 관점에서 제작된 패키지
#그래프 중첩 및 각종 서식 지정 편리

df= data.frame(xx= 1:10,
               yy= c(1:4, 5:3, 6:8))
library('ggplot2')
ggplot(data= df, aes(x=xx, y=yy))+ geom_point()
ggplot(df, aes(xx,yy))+ geom_point()
ggplot() + geom_point(data= df, aes(x= xx, y=yy)) #우우
ggplot() + geom_point(data= df, aes(xx,yy))

ggplot() + geom_point(df, aes(xx, yy)) # 에러가 뜬다. 
ggplot() + geom_point(mapping= aes(xx, yy), data= df)#원래 이게 정석


#기본그래프= geom_point(), geom_col(), geom_line()



#문제1 기본그래프를 사용하여 AWS_sample.txt 파일의 첫 200개 행의 데이터만 사용하여 TA변수를 대상으로 plot()함수로
#선그래프 그리시오
df= read.csv('./dataset/AWS_sample.txt', sep = '#')
head(df)
plot(df[1:200,'TA'])
plot(df[1:200,'TA'],type= 'l')

#문제2 기본그래프를 사용하여 AWS_sample.txt 파일의 첫 200개 행의 데이터만 사용하여 TA변수를 대상으로 ggplot()함수로
#선그래프 그리시오

a= df[1:200,]
a
ggplot(data= a,aes(x= 1:200, y= TA )) + geom_line()













