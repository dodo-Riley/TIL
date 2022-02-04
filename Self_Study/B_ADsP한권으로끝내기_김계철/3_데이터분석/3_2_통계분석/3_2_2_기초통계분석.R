## 기술통계
data(iris)
head(iris) # 데이터의 기본 6행을 보여줌
head(iris,3) # 데이터의 기본 3행을 보여줌
tail(iris) # 데이터의 마지막 6행을 보여줌
head(iris,3); tail(iris,3) # 데이터의 처음 3행, 마지막 3행을 보여줌

summary(iris) # 데이터의 컬럼에 대한 전반적인 기초 통계량을 보여줌줌
summary(iris$Sepal.Width) # iris데이터의 Sepal.Width 컬럼의 기초 통계량을 보여줌줌

mean(iris$Sepal.Length) # 평균
median(iris$Sepal.Length) # 중위수
sd(iris$Sepal.Length) # 표준편자
var(iris$Sepal.Length) # 분산
max(iris$Sepal.Length) # 최대값
min(iris$Sepal.Length) # 최소값
quantile(iris$Sepal.Length,1/4) # 1사분위수
quantile(iris$Sepal.Length,3/4) # 3사분위수

# 다른 데이터로 다시 해보기
library(MASS)
data(Animals)
head(Animals)
summary(Animals)
quantile(Animals$body)
quantile(Animals$brain)

## 회귀분석
# attitude데이터활용 다중회귀분석
data("attitude")
tail(attitude)

out<-lm(rating~complaints+privileges+learning
        +raises+critical+advance,data=attitude)
out<-lm(rating~.,data=attitude)

summary(out)

# chickweight 데이터 활용 단순회귀분석
data("ChickWeight")
head(ChickWeight)
chick = ChickWeight[ChickWeight$Chick==1,] # 
m1 = lm(weight~Time,data=chick)
summary(m1)

## 잔차분석을 통한 회귀분석의 모형 가정
data(cars)
m = lm(dist~speed, cars)
summary(m)
par(mfrow=c(2,2))
plot(m)

## 다항 회귀 분석
x <- c(1,2,3,4,5,6,7,8,9)
y <- c(5,3,2,3,4,6,10,12,18)
df1 <- data.frame(x,y)
m1<-lm(y~x,df1)
par(mfrow=c(2,2))
plot(m1)

x2 = x^2
df2 = cbind(x2,df1)
plot(lm(y~x+x2,df2))

## step() 함수를 이용한 단계적 변수 선택
x1 = c(7,1,11,11,7,11,3,1,2,21,1,11,10)
x2 = c(26,29,56,31,52,55,71,31,54,47,40,66,68)
x3 = c(6,15,8,8,6,9,17,22,18,4,23,9,8)
x4 = c(60,52,20,47,33,22,6,44,22,26,34,12,12)
y = c(78.5,74.3,104.3,87.6,95.9,109.2,102.7,72.5,93.1,115.9,83.8,113.3,109.4)
df = data.frame(x1,x2,x3,x4,y)
step(lm(y~1,df), scope=list(lower=~1,upper=~x1+x2+x3+x4), direction='forward')

## 릿지회귀에서 람다값의 크기 영향 확인
install.packages('ridge')
library(ridge)
data('longley')
names(longley)[1] = 'y'
mod = linearRidge(y~.-1, data=longley, lambda = 'automatic')
options(scipen=999)
summary(mod)
install.packages('genridge')
library(genridge)
lambda=c(0,0.005,0.01,0.02,0.04,0.08)
r = ridge(y~.,longley,lambda=lambda)
traceplot(r)
