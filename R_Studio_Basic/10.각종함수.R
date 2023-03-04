aa= c(1, 2, NA, 5)
mean(aa, na.rm = TRUE)
aa
#산술 함수

nums= c(2, 5, 7, 9, 20)
nums

min(nums) #최소
max(nums) #최대
mean(nums)  #평균균
median(nums) #중앙 값=7
cumsum(nums) #누적 값 ( 2+5하고 그다음 7이랑 더하고 그다음 9랑 더하고)

nums2= c(-2, 4, 6)
nums2

abs(nums2) # 절대값
log(abs(nums2)) # 로그 
log(abs(nums2), base = 2) #로의 밑에 2를 배치

exp(1) #exp = expernantial 오일러수
exp(2) #제곱곱

sqrt(abs(nums2)) # sqrt= 루트 씌운것과 비슷

df= read.csv("./dataset/diabetes.csv")
head(df, 2)

quantile(df$Pregnancies) #백분위 별 데이터 출력
quantile(df$Pregnancies, probs = 0.99) #제 99퍼 백분위 수 자료 호출 상위 1프로
quantile(df$Pregnancies, probs= c(0.01, 0.99)) #하위 1퍼센트와 상위 1퍼센트 출력

head(df, 2)

df[,"BMI_round"] = round(df$BMI) #colnames에 BMI_round 추가후 계산값 입력
head(df, 2)

# 문제1 bike.csv 데이터를 불러와서 temp 변수의 평균을 구하시오
df2 = read.csv("./dataset/bike.csv")
head(df2)
head(df2$temp) #=head[df2[,temp]]와 같음
df2[,'temp_average'] = mean(df2$temp)
head(df2, 2)


#문제2 AWS_sample.txt 파일의 Wind 변수의 최소값을 구하시오
df3= read.csv("./dataset/AWS_sample.txt", sep = '#')
head(df3)
min(df3$Wind)
#문제 3 AWS_sample.txt 파일의 TA 변수의 중위수(중앙값)를 구하시오.

median(df3$TA)







