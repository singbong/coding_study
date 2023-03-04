#객체 대표적으로 1차원 벡터, 메트릭스, 데이터프레임, 리스트 존재

#Ls() 함수로 현재 등록된 객체 목록 확인 가능
#object.size() 함수로 객체 용량 확인 가능
View(globalenv())
aa= 123
bb= 1:3
object.size(bb)
object.size(1:3000) #바이트 크기 출력
#ls() / base / pattern / 등록된 객체 목록을 출려하며, pattern 인자로 필터링 가능
#object.size() / utils / 특정 객체의 용량 확인 가능
#format() / utils / units / object.size() 함수의 출력물을 units 인자로 활용 하여 kb, mb 등 각 자료 단위로 표기 가능
#rm() / base / 등록된 객체를 제거하고자 할 때 사용

format(object.size(1:300000), units = "Mb") # 키로바이트 값을 출력하는 object.size에 format을 덮어씌운것

format(object.size(1:300000), units= 'Kb')
?format
format(object.size(1:300), units= 'auto')
?rm
rm(bb) #bb객체 삭제


#01벡터
c(1, 2, 3)
c(1, 2, 'a') # 문자와 숫자가 결합되면 숫자가 문자로 통일이 된다.

c("a" = 100)
c(A = 100)
vec= c( 'A' = 100, 'B' = 200, 'C' = 300) #named vector 이름이 부여된 벡터
vec[1]  #파이썬의 슬라이싱 개념과 비슷한거 같음 단, R은 인덱스가 0번부터가 아닌 1번 부터 시작된다.
vec[2:3] #두번째에서 3번째 까지 출력
vec[c(1,3)]

#대괄호: 추출
vec[2] = 'kkk' #인덱스 수정
vec #kkk가 들어가면서 원소들이 문자열로 바뀜

vec1 = c(3, 4, 5)
vec2= c(8,9)
vec_concat = c(vec1, vec2)
vec_concat[1:3]
vec_concat
#02
#c()
#c(..., recursive = FALSE, use.names = TRUE)
#This is a generic function which combines its arguments.
#names()
vec_new = c("a"=22, "b"=33)
vec_new

names(vec_new) #names는 벡터에 부여된 이름들만 추출 파이썬으로 치면 vec_new.keys()와 비슷
names(vec_new)[1]
names(vec_new)[c(1, 2)]
names(vec_new)[1:2]

names(vec_new)[2] = "sibal"
vec_new

#seq()
seq(1, 4)
seq(1, 4, 1)
seq(from = 1, to = 4, by= 1)
seq(from = 1, to =4, by= 0.5) #1부터 4까지 0.5씩 연속 증가해서 출력
seq(1,4,0.5) #윗줄 코드와 동일

#rep() replicate 복제
rep(2:4, 2)
rep(2:4, times = 2)
rep(1:3, 4)
rep(1:3, times = 4) #1에서 3까지 4번 반복
rep(times= 2, x= 1:3) #argument를 명시 해줬기 때문에 작동된다. 가독성 증가
rep(1:3, each= 2) #각 인덱스를 반복하고 다음 인덱스로 이동

#length() 원소의 갯수를 나타냄
length(c(4,6,8))
length(c('a', 1, 'v', 3, 'wss'))

letters #소문자
letters[1:4]
LETTERS #대문자
LETTERS[1:4]

length(LETTERS)

#unique() 중복 원소를 삭제
vec_dup = c(1, 1, 3, 3, 5, 6)
length(vec_dup)
unique(vec_dup)
length(unique(vec_dup))


# : 는 1씩 증가 또는 감소 
abc = c(3:-3)
abc
1.5:4 # 1.5부터 4이하 1씩 증가

#03메트릭스
matrix(1:4)
matrix(1:4, nrow = 1) #row = 가로 nrow= number of rows
matrix(1:4, nrow = 2)
matrix(1:4, ncol = 1) #col= 세로
matrix(1:4, ncol = 2)
matrix(1:4, ncol = 2, byrow = TRUE)

mat= matrix(1:4, nrow =2)
mat
rownames(mat)
colnames(mat)
dim(mat) # 행렬이 몇 곱하기 몇인지 알려줌
diag(mat) # 대각 원소 출력
eigen(mat) # 원소 고유 값 출력
?matrix

mdat = matrix(c(1,2,3, 11,12,13), nrow = 2, ncol = 3, byrow = TRUE,
               dimnames = list(c("row1", "row2"),
                               c("C.1", "C.2", "C.3")))
mdat
rownames(mdat)
colnames(mdat)
colnames(mdat) = c('a1','a2','a3')
mdat

mat[1,] #첫번쨰 row
mat[,2] # 두번쨰 col
mat[1,2]
mat[2,2]
mat[1,1] = 'kkk' #수정
mat

matrix(1:10)
tew = matrix(1:15, nrow = 5, ncol = 3)
tew[,3]
dim(tew)
diag(tew)
