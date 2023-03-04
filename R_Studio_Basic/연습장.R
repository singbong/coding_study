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


as.POSIXct('2023-03-02 15:00:00')
as.Date('2022-03-02')

months(as.Date('2022-02-03'), abbreviate = TRUE)
as.Date(500, origin = '2023-03-02')

df = data.frame(obs= 1:4, passed= c(10,15,20, 30))
df
df$"origin" = as.Date(df$passed,
                      origin = '2022-03-02')
df
df= df[,-grep(pattern = 'origin', colnames(df))]
df
weekdays(as.Date('2023-03-02'))
weekdays(as.Date('2023-03-5'), abbreviate = TRUE)
library('lubridate')
ymd(20230302)
ymd(20230302)
ymd_h('20230302 13')

strptime('2023-05-06 16+12+13', format='%Y-%m-%d %H+%M+%s' )
year('2022-02-05')

#order(), aggregate() apply(), ifelse(), table()



df_date = data.frame(obs= 1:4, 
                     passed= 4:7)
df_date$"passed_date" = as.Date(df_date$passed, origin = '2023-03-02')
df_date

df_date$'wday'= weekdays(df_date$passed_date)
df_date
df_date= df_date[order(df_date$passed), ] #오름 차순
df_date
df_date= df_date[order(df_date$wday, decreasing = TRUE),]
df_date


df_3= read.csv('./dataset/bike.csv')
head(df_3)
df_4= aggregate(data= df_3, registered ~ humidity, FUN = 'mean' )
df_4[grep(pattern = max(df_4$registered), df_4$registered),]
