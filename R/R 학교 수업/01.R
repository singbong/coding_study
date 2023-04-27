a= c(1,2,3,4,5, 10, 100)
a
sum(a %in% 3)

seq(1,20, 3)


rep(1:3, 2)

names(a)
mean(a, trim = 0.55)

summary(a)

diff(range(a))

rownames(iris)
colnames(iris)
dim(iris)
nrow(iris)

m= matrix(1:20, nrow = 4, ncol = 5)
m= data.frame(m)
colnames(m)= c('a','b','c','d','e')
m
class(m)
