#01필터링 1차원 벡터 데이터 필터링링
aa = c(2,4,6,8)
aa
aa[c(2,4)]

aa[aa == 4]
aa[aa != 4]

df = data.frame(aa= 1:3,
                bb= c('a', 'b', 'c'))
df
df[c(1:3),]
df[c(TRUE, FALSE, TRUE),]
df[df$aa !=2,]
df[(df$bb == 'a') | (df$bb == "b"),]

#02 data.frame의 신규 변수 생성성
df_1 = data.frame(aa= c(1:3),
                  bb= c(4:6))
df_1
df_1$"new_col" = df_1$aa * df_1$bb
df_1
df_1 = df_1[,-grep(pattern = 'new_col', colnames(df_1))] # new_col col삭제
df_1
df_1[,5] = 555 # R은 기본적으로 rowname의 변수명이 숫자로 시작하는 것을 허용하지 않음.

#03 시간데이터 핸들링

#as.PSIXct(), as.Date, months, weekdays, ymd(), ymd_h(), strptime(), year, month, wdaym, hour, order, aggregate

as.POSIXct("2077-12-31")
as.POSIXct("2077-12-31 23:59:59") #결과 "2077-12-31 23:59:59 KST"
as.Date("2077-12-31")

vec_date = as.Date("2077-12-31")
class(vec_date) #결과 Date 문자열이 아니라 date 형으로 나옴

as.Date(50000)
as.Date(50000, origin = "1900-01-01") # 1900/01/01부터 50000일이 지난 시점 날짜 출력

df_date = data.frame(obs= 1:4, 
                     passed= 4:7)
df_date
df_date$"passed_date" = as.Date(df_date$passed, origin = '2023-03-02')
df_date

months(as.Date('2030-01-01')) # months 안에 파라미터는 date 형만 입력 받음
months(as.Date('2030-01-01'), abbreviate = TRUE) #abbreviate는 '월'여부
as.numeric(months(as.Date('2030-01-01'), abbreviate = TRUE)) #윗줄 코드 months 는 문자열로 반환 근데 보통 정수로 쓰이니 변환

weekdays("2023-03-02")
weekdays(as.Date('2023-03-02'))
weekdays(as.Date('2023-03-02'), abbreviate = TRUE)

df_date

df_date$'wday'= weekdays(df_date$passed_date)
df_date

#lubridate 패키지 함수

library('lubridate')

ymd(20300101)
ymd('20300602') #알아서 알아 들음
ymd('2030@1@1')
ymd_h('20300101 13') #2030-01-01 13:00:00 UTC

as.POSIXct('2030-01-02 13') #"2030-01-02 KST"
strptime('2030-01-02 13',format= '%Y-%m-%d %H') #파이썬에도 이런거 있음

date_01 = ymd("2030년 1월 1일")
date_01
year(date_01)
month(date_01)
day(date_01)
wday(date_01, week_start = 1) #week start = 1 은 월요일을 시작점으로 두겠다 이거를 가장 많이씀
wday(date_01, label = TRUE)
wday(date_01, label = TRUE, week_start = 1)
hour(ymd_h("2023-03-02 15"))

#04 정렬
#order() 함수
df_date = data.frame(obs= 1:4, 
                     passed= 4:7)
df_date$"passed_date" = as.Date(df_date$passed, origin = '2023-03-02')
df_date

df_date$'wday'= weekdays(df_date$passed_date)
df_date
df_date= df_date[order(df_date$passed), ] #오름 차순
df_date
df_date= df_date[order(df_date$passed, decreasing = TRUE), ] #내림차순
df_date= df_date[order(df_date$wday, decreasing = TRUE),]
df_date

#aggregate() 함수

#aggregate(data= df, y~x1+x2, FUN= "fun_name")
df= iris
head(df)
aggregate(data= df, Sepal.Length~Species, FUN= 'mean')# species별 length 평균균

bike = read.csv("./dataset/bike.csv")
head(bike)
aggregate(data = bike, temp ~ season + weather, FUN = 'mean') #이런경우 season과 weather 별 temp 출력
a=aggregate(data = bike, temp ~ season, FUN = 'mean')
b=aggregate(data = bike, temp ~ weather, FUN = 'mean')
head(a)
head(b)

head(bike, 20)
avg= aggregate(data = bike, registered ~ hour(datetime), FUN = 'max' ) #avg 변수에 시간별 등록수 평균을 저장
avg
grep(pattern = max(avg$registered), avg$registered)
avg[grep(pattern = max(avg$registered), avg$registered),] #대여수가 가장 많은 시간 추출

#apply for 반복문을 대체 할수 있는 대표적인 함수
# apply(X = df, MARGIN = 1, FUN= 'sum') 마진 1은 row방향 연산 2는 col방향 연산
df= iris
head(df)
apply(X= df, MARGIN = 2, FUN = 'max')
df$'mean'=apply(X= df[,-grep(pattern = 'Species', colnames(df))], MARGIN = 1, FUN = 'mean')# species가 str형태라 안됌
head(df)

#일괄 계산 
#ifelse()

ifelse(test= 1:4 >2,  #결과 "??" "??" "!!" "!!"
       yes = '!!',
       no='??')
df= iris
head(df)
df$'is_setosa' = ifelse(test= df$Species=='setosa',
                        yes = 'TRUE',
                        no= 'FALSE')
tail(df, 20)
table(df$Species, df$is_setosa) # 복습하자

#문제1 
'''
특정 일자에 상대 습도가 100이라면 비 또는 눈이 왔을 가능성이 있다.
주어진 데이터를 기준으로 비 또는 눈이 왔을 가능성이 있는 날은 총 며칠인가?
'''
df= read.csv('./dataset/bike.csv')
head(df)
df[grep(pattern = 100, df$humidity),]
sum(grepl(pattern = 100, df$humidity))

df[,'date']= as.Date(df$datetime)
quantile(df$humidity)
df_agg = aggregate(data= df, humidity ~ date, FUN = 'max')
df_agg
sum(grepl(pattern = 100, df_agg$humidity))
library('lubridate')
head(df)
df_m = aggregate(data= df, count  ~ hour(df$datetime) + wday(df$datetime, label = TRUE), FUN = 'mean')
head(df_m)
df_m
