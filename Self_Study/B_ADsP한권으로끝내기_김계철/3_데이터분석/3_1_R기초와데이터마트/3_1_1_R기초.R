# 기초적인 연산
1+2
3-1
2*2
4/2
3^3
1+2;3+4
x=1;y=1;x+y

# 벡터
c(1,2,3)+2
c(1,2,3)+c(4,5,6)
c(1,2,3)+c(4,5,6,7)
1:5
6:9
seq(5)
seq(1,5)
seq(1,2,0.1)
seq(5,1)
rep(1,3)
rep(c(1,2,3), times=2, each=2)
rep(c(1,2,3),c(1,2,3))
rep(1:5, times=2, each=2, length.out=5)
sequence(3)
sequence(1:5)
sequence(c(1,5,3))

# 행렬
m = matrix(c(1,2,3,4,5,6), nrow=3, ncol=2, byrow=FALSE, dimnames=NULL)
dimnames(m) = list(c('r1','r2','r3'),c('c1','c2'))
m
a=c(10,10)
b=c(10,10,10)
rbind(m,a)
cbind(m,b)

# 데이터프레임
a=c(1,2,3)
b=c('a','b','c')
c=c(TRUE, FALSE, FALSE)
df = data.frame(first=a,second=b,third=c)
df

# 배열
array(1:12,dim=c(3,4))
array(1:12,dim=c(2,2,3))

# 리스트
x=list(name='riley', tel='3333-3333')
x

# R의 기초함수
rep(1,3)
seq(1,3)
seq(1,11,2)
seq(1,10,length=8)

# 기초적인 행렬 계산
a=1:5
a+a
a-a
a*a
a/a
a=c(1,2,3)
t(a)
a%*%t(a)
b=a%*%t(a)
c=3*b
solve(c)
a=matrix(5:20, nrow=4)
solve(a)
a=matrix(c(23,41,12,35,67,1,24,7,53),nrow=3)
solve(a)
3*a
c=1:10
mean(c)
var(c)
sd(c)
sum(c)
median(c)
log(c)
a=1:10
b=11:20
cov(a,b)
cor(a,b)
summary(a)

# 데이터 핸들링
b<-c('a','b','c')
b
b[2]
b[-3]
b[c(1,3)]
b[1:2]

# 반복문과 조건문
a<-c()
for(i in 1:5)
{a[i]=i^2}
a
x=1
while(x<5)
{x=x+1
print(x)}
gender=c('1','2','2','2','1')
gender=ifelse(gender=='1',T,F)
gender

# 사용자 정의 함수
foruse=function(number){
  sum=0
  for(i in 1:number){
    sum=sum+i
  }
  print(sum)
}
foruse(6)

# 기타 유용한 기능들
a=1:5
b=c('a','b','c','d','e')
paste(a,b,sep='/')
a=c('one','two','three')
substr(a,1,2)
a=c(1,2,3)
as.data.frame(a)
as.list(a)
as.matrix(a)
as.factor(a)
as.numeric(a)
as.character(a)
as.integer(a)
as.logical(a)
as.Date('2021/01/24')
as.Date('01/24/2021', format='%m/%d/%Y')
Sys.Date()
format(Sys.Date(),'%a')
format(Sys.Date(),'%b')
format(Sys.Date(),'%y')
format(Sys.Date(),'%Y')

# 산점도 그래프
math=c(95,65,80,92,60,75,88,100,75,68)
science=c(90,70,80,95,65,70,85,95,70,60)
plot(math,science)

# 산점도 행렬
pairs(iris[1:4], main="Anderson's Iris Data--3 species",
      pch=21, bg=c('red','green3','blue')[unclass(iris$species)])

# 히스토그램
a=c(1,2,3,4,5,6,7,6,5,4,5,8,10,4,3,2,1)
hist(a)
hist(a, breaks=3)
hist(a, probability=T)
hist(a, probability=T, main='test', ylim=c(0,0.2))

# 박스플롯
boxplot(a)
