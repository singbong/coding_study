df= data.frame(x=c(1,3,5,6,7), y=c(2,4,6,10,9))
df
dist(df, method= 'euclidean', p=2)

data(trees)
trees
round(dist(trees),2)
dist(scale(trees, center=FALSE))

round(dist(scale(trees, center=FLASE)),2)


x=matrix(rnorm(100*3), ncol=3)
x
Sx= cov(x)
Sx
MD= mahalanobis(x, colMeans(x),Sx)
MD
round(MD,2)


# 분산과 공분산 행렬
# mtcars 데이터에 대한 분산, 공분산 행렬 구하기

data(mtcars)
str(mtcars)
cov(mtcars[, c('disp','hp','wt','qsec')])
cor(mtcars[,c('disp','hp','wt','qsec')])


# am==0 인 경우의 4개 변수의 분산, 공분산행렬

cov(subset(mtcars, am==0)[,c('disp','hp','wt','qsec')])
cor(subset(mtcars, am==0)[,c('disp','hp','wt','qsec')])


# 결측값의 대치(inputation)

data(airquality)
?airquality
str(airquality)

air= airquality[,1:4]
air[11:15,3] = NA
air[51:55,4]= NA
air
summary(air)


library(mice)
md.pattern(air)


library(VIM)


aggr(air, col= c('skyblue','red'))

aggr(air, col=c('skyblue','red'), number=T, sortVars=T)

aggr(air, col=c('skyblue','red'), number=T, sortVars=T,
     labels=names(air), cex.axis= 0.7, gap=3,
     )

marginplot(air[c(1,2)])


air.MI = mice(air, m=5, maxit= 50, meth='pmm', seed=200)

ls(air.MI)

summary(air.MI)

air.com = complete(air.MI, 1)
air.com

xyplot(air.MI, Ozone ~ Solar.R + Wind + Temp, pch=18, cex=1)


densityplot(air.MI)
stripplot(air.MI)
stripplot(air.MI, pch=20, cex=1.2)
#이러한 데이터 셋으로부터 특정 모형을 적합시킨 뒤 결합


fit1= with(air.MI, lm(Temp~ Ozone+Solar.R+Wind))
summary(pool(fit1))

air.MI2= mice(air, m=50, seed=100)
fit2= with(air.MI2, lm(Temp~ Ozone+Solar.R+Wind))
summary(fit2)

