#data.frame()
data.frame(aa = 1:3, bb = 3:5)
df = data.frame('aa'= 1:3, 'bb' = 3:5)
df
df$aa #df 객체의 aa 변수
df[,1] #모든 row, 첫번째 column
df[,"aa"] #모든 row, aa column 출력
df[c(1,3),] # 1,3 번쨰 row의 모든 col
df[c(1,3),2] # 1, 3 번째 row, 두번째 col

df$aa[1]
df[1, "aa"]

df[1, 'aa'] = 100
df
df[1, 'bb'] = 'kkk'
df
df$bb
df$aa

summary(df)
rownames(df)
colnames(df)
nrow(df) #obs. = observations.
ncol(df)
dim(df)
matrix(c(1,2,3,4,5,6), nrow = 2, ncol = 3)
df
colnames(df)[1] = "class"
df

#list

list(aa= 1:3)
list("aa" = 1:3)

list(aa=1:3, bb= 2:4)
list(aa= 1:3, bb= matrix(1:4, nrow= 2, ncol = 2, byrow = TRUE, list(c('aa', 'bb'),c('cc','dd'))))

ls= list(aa= LETTERS[1:3], 
        ff= list(bb= c(3:6),
             cc= data.frame(dd=1:3, ee= 2:4)))

ls
ls$aa
ls$ff
ls$ff$bb

length(ls)
names(ls)
names(ls$ff$cc)
colnames(ls$ff$cc)
rownames(ls$ff$cc)
rownames(ls$ff$cc)
str(ls) #객체 구조
list(ls)
unlist(ls)


#벡터 리사이클링

data.frame(aa= 1:4, bb=rep(1:2, times = 2))
df1= data.frame(aa= 1:4, bb = 1:2) #비어잇으면 자동으로 복제
df1
df1[, 'new'] = 1
df1
df1$'abc' = 4:5 # abc 에 'abc' col 생성 후 4,5를 채우고 남은 빈칸 4,5 복제
df1
df1[,'mul'] = df1$aa + df1$bb
df1$aa
df1$bb
df1$aa + df1$bb
df1
