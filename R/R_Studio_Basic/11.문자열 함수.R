 #문자열 처리함수
#nchar(), print(), sprintf() , grep(), grepl(), gsub() paste() paste0() substr() strsplit()

#nchar
nchar("asdf")
nchar(1561) # 자동으로 문자열로 변환

df= iris
head(df, 2)
colnames(df)
nchar(colnames(df))
head(df,2)

unique(df$Species) #중복 colname 삭제 ,factor
head(df, 2)
class(unique(df$Species)) #factor
nchar(unique(df$Species)) #char vector를 요구함

nchar(as.character(unique(df$Species))) #변환후 nchar

head(as.character(df$Species), 2)
nchar(as.character(df$Species)) # char vector 요구 에러
nchar(as.character(unique(df$Species))) # species에서 중복을 제거한것들을 char화
#한 후 각 문자열의 갯수 출력
head(df, 2)
df$"nchar" =nchar(as.character(df$Species))
head(df, 2)
head(df, 2)
df= df[,-(length(colnames(df)))] # 해당 열 삭제 방법법
head(df, 3)

#print()
print('asdf')
print(1234)

#sprintf()
8:20
sprintf(fmt = '%02d', 8:20) # 2자리 정수 형태로 8부터 20 출력
sprintf(fmt = '%04d', 8:20)
?sprintf

#grep()

df_text = data.frame(obs= 1:3,
                     text = c("aaa", "abc", "bbb"))
head(df_text)
grep(pattern= 'c', df_text$text) #결과: 2 / text 객체의 변수의 원소중에서 c라는 글자가 포함된 row의 위치를 추출

head(df, 3)
df = df[,-grep(pattern= 'Species', colnames(df))] #grep응용
head(df, 3)

#grepl()
grepl(pattern= 'c', df_text$text)
df_text
df_text[grepl(pattern= 'c', df_text$text),]
df_text[c(FALSE, TRUE, FALSE),] #c()를 써야만 원하는 값 출력
sum(grepl(pattern= 'c', df_text$text))
#df_text 객체의 text 변수의 원소 중에서 c라는 글자가 포함된 원소의 갯수를 세는 것

#gsub() 
gsub(pattern = 'abc',
     replacement = '@@@',
     x= 'abc_kkk') #x 변수의 abc 라는 패턴이 있으면 그부분을 @@@로 바꾸고 싶어

df_text$text
gsub(pattern = 'b',
     replacement = '@',
     x= df_text$text)


#paste()
paste("aa", 'bb')
paste("aa", 'bb', sep= '-')
paste("aa", 'bb', sep= '')
paste(c(1, 2, 3, 4, 5), sep= '-')
paste(c(1, 2, 3, 4, 5), collapse = '-') #collapse는 1차원 벡터로 데이터가 들어올때만 작동한다 pastec(1, 2, 3, 4, 5, collapse= '-')

df
head(df,2)
paste(df$Sepal.Length[1:3],
      df$Sepal.Width[1:3], sep = '@@')



#paste0()

paste0("sample", ".csv") # 걍 두개 원소 붙이기
paste0("sample", 1:3, ".csv") # 3개씩 복사
paste0("sample", 8:12, ".csv")
paste0("sample", sprintf(fmt = '%02d', 8:12), ".csv") #자릿수 맞추기

#substr()

file_names = paste0("sample_", sprintf(fm = '%02d', 8:12), ".csv")
file_names

substr(x= file_names, start = 1, stop = 6) #파일 이름들의 문자열 1에서 6까지지
substr(x= file_names, start = 8, stop = 9)

as.numeric(substr(x= file_names, start = 8, stop = 9))
sum(as.numeric(substr(x= file_names, start = 8, stop = 9)))


#strsplit()

strsplit(file_names, split= "_")
file_split = strsplit(file_names, split= "_") #_기준으로 쪼개기
file_split
file_split[[1]][2] #file_split에 1번에 두번째 인덱스

unlist(file_split)
file_split_ul = unlist(file_split)
df_file = data.frame(obs= 1:length(file_names),
                     file_name = file_names)
df_file
a= file_split_ul[seq(1, length(file_split_ul), 2)]
b = file_split_ul[seq(2, length(file_split_ul), 2)]
df_file[,"split1"] = a
df_file[,"split2"]= b
df_file








