#getwd() 현재 작업폭더 경로를 확인하는 함수
#setwd() 현재 작업폴더 경로를 변경하는 함수


getwd()
setwd("C:/Users/Sin/Desktop/git 자료")
#setwd('..') 파이썬처럼 상위폴더를 의미
getwd()

#파일 및 폴더 목록 확인
#recursive 인자는 폴더의 하위 폴더까지 탐색하여 결과를 출력

list.files()
getwd()
list.dirs()
dir()

list.files(pattern = "csv")# 파일명 또는 폴더명에 csv가 들어가는 것만 검색
list.files(pattern = '원소')

#3 파일입력(load, read)
#대표적인 파일 확장자= csv, tsv, txt csv= comma-separated values, tsv= tab ....

df= read.csv("./dataset/AWS_sample.txt")
head(df)

df_aws = read.csv("./dataset/AWS_sample.txt", sep = '#')
head(df_aws) #head()는 상당읜 6개의 row를 출력
?head #head(x, n = 6L, ...) 기본값이 6이기 떄문에 6개의 row출력

head(df_aws, 3) #3줄만 출력

tail(df_aws) # tail꼬리 뒤에서 6개 출력
tail(df_aws, 3) #뒤에서 3개만 출력

df_bike = read.csv("./dataset/bike.csv")
head(df_bike)

library('readr')
#만약 에러가 나면 install.packages("readr")
df_bike_2 = read.csv("./dataset/bike.csv")
head(df_bike_2)

class(df_bike_2)

df_b= as.data.frame(df_bike_2) #data.frame 이 아닌 것을 data.frame 으로 형변환환
df_b
head(df_b)
class(df_b)

library("data.table")
df_bike_3 =fread("./dataset/bike.csv") 
head(df_bike_3) #head(df_b) 와 미세한 차이 가있음
class(df_bike_3)  # data.table 과 data.frame 존재

df_b_2 = as.data.frame(df_bike_3)# df_b_2= df_b
class(df_b_2)
head(df_b_2)

fread("./dataset/bike.csv", data.table = FALSE, nrows= 2) #data.table은 끄고 2개의 row만 불러오기 기본값은 TRUE
library("readxl")
# read_excel() 엑셀 파일 읽기

#4 파일 출력(save, write)
df_sample = matrix(c(1:10), nrow = 2, ncol = 5,
                   dimnames = list(c('가','나'),c('a','b','c','d','f'))
                   )

write.csv(df_sample, "./dataset/write_csv_sample_01.scv")
write.csv(df_sample, "./dataset/write_csv_sample_02.scv",
          row.names= FALSE) #rownames 저장은 기본값이 TRUE이다.근데 FASLE로 해라

#인코딩
#파일을 저장하고 불러올 때 인코딩이 일치하징 ㅏㄶ으면 글자가 제대로 조합되지 않는 현상 발생

write.csv(df_sample, "./dataset/write_csv_sample_02.scv",
          row.names= TRUE, fileEncoding = "UTF-8")
write.csv(df_sample, "./dataset/write_csv_sample_02.scv",
          row.names= TRUE, fileEncoding = "euc-kr")

list.files(path = "./dataset", pattern = "csv")













