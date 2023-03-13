z= matrix(1:20, nrow=4, ncol=5, byrow = TRUE)
z
x=1:4
y=5:8
z= matrix(1:20,nrow = 4, ncol = 5)
z
m1= cbind(x,y)
m1
m2= rbind(x,y)
m2


z= matrix(1:20, nrow = 4, ncol = 5)

df1= data.frame(a= c(1:4), b=c(5,8))
df1

score= matrix(c(90,85,69,78,
              85,96,49,95,
              90,80,70,60), nrow = 4, ncol = 3)
score
rownames(score)= c('Jhon','Tom', 'Mark', 'Jane')
colnames(score)= c('영어','수학','과학')
score

score['Jhon','수학']
rownames(score)
colnames(score)

df2= data.frame(city= c('Seoul','Tokyo','Washington'), rank=c(1,3,2))
df2

df3= iris
df3[,c(1,5)]
df3[c(1,5),]

dim(df3)
nrow(df3)
ncol(df3)
colnames(df3)
head(df3, 10)
tail(df3, 4)

str(df3)
df3[,5]

df3[-grep(pattern = 'virginica', df3$Species),]

unique(df3$Species)
table(df3$Species)


colSums(df3[,-5])
colMeans(df3[,-5])







