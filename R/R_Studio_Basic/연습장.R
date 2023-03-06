#nchar(),print(), sprintf() , grep(), grepl(), gsub() paste() paste0() substr() strsplit()

df= iris
head(df, 3)

nchar(as.character(unique(df$Species)))
head(nchar(as.character(df$Species)), 3)

sprintf(fmt = '%03d', c(1:5))      
df
grep(pattern = 'virginica', df$Species)

head(df, 5)
df$"Result" = nchar(as.character(df$Species))
head(df)
grep(pattern = 'Result', colnames(df))



df1= iris
df1 = df1[-grep(pattern = 'se', df1$Species),]
df1 = df1[-grep(pattern = 'ver', df1$Species),]
df1
df$Species = gsub(pattern = 'versicolor',
                  replacement = 'sibal',
                  x=df$Species)
df$Species= gsub(pattern = 'virginica',
                  replacement = 'good',
                  x=df$Species)

df$Species
df
head(df)

#paste() paste0() substr() strsplit()

paste(df$Sepal.Length[1:6], df$Sepal.Width[1:6], sep = '-')
paste(c(1,2,3,4,5), collapse = 'a')

paste0("sample", sprintf(fmt = '%02d', 1:5), ".csv")

b= paste0("sample#", sprintf(fmt = '%02d', 1:5), ".csv")
b
substr(x = b, start = 8, stop = 9)

c= strsplit(b, split = "#")
c
f= unlist(c)
f
a1= f[seq(1, length(f), 2)]
a2= f[seq(2, length(f), 2)]
a1
a2
d= data.frame(obs= 1:length(f), file_name= b)
d
d$"split1" = a1
d$"split2" = a2
d

#문제1 df에 species col에 vir이 들어 가는 row는 전부 삭제

#문제2 df에 species col에versicolor가 들어가는 row들은 전부 sibal로 바꾸기
df= iris
head(df)
df$'Species' =gsub(pattern = 'versicolor', replacement = 'sibal', x = df$Species)
df

#문제3 df$Sepal.Length, df$Sepal.Width 해당하는 1:6 row '-'로 구분지어 붙이기

#문제4 


#as.PSIXct(), as.Date, months, weekdays, ymd(), ymd_h(), strptime(), year, month, wday(), hour(), order(), aggregate()


#order(), aggregate() apply(), ifelse(), table()





#문제1 기본그래프를 사용하여 AWS_sample.txt 파일의 첫 200개 행의 데이터만 사용하여 TA변수를 대상으로 plot()함수로
#선그래프 그리시오
getwd()
df= read.csv('./R/R_Studio_Basic/dataset/AWS_sample.txt', sep= '#')
head(df)
df_TA = df$TA[1:200]
df_TA

plot(x= 1:200, df_TA, type = 'l')



#문제2 기본그래프를 사용하여 AWS_sample.txt 파일의 첫 200개 행의 데이터만 사용하여 TA변수를 대상으로 ggplot()함수로
#선그래프 그리시오
library('ggplot2')
ggplot(data= df[1:200,], aes(x= 1:200, y= TA)) + geom_line()






