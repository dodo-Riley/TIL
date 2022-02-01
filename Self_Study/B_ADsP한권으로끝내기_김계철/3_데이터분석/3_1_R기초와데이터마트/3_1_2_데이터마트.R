## reshape 활용
install.packages('reshape')
install.packages('reshape2') # 패키지 설치
library(reshape)
library(reshape2) # 패키지 호출
data(airquality) # 데이터 호출
colnames(airquality) = tolower(colnames(airquality)) # 컬럼명 소문자로 변경
head(airquality,4) # 가장 처음부터 4줄까지 출력

# id에 지정된 변수를 기준으로 나머지 변수를 variable로 만듬
# 그리고 각 variable에 해당하는 value값이 자동으로 저장
T = melt(airquality, id=c('month','day'), na.rm=TRUE)
T

cast(T, day~month~variable)# 행은 day, 열은 month, 각 variable에 대해 값 배열

b = acast(T,month~variable,mean) # 각 변수들의 month 평균
b

d = cast(T,month~variable,mean,margins=c('grand_row','grand_col'))
d # 모든 행과 열에 대한 소계 산출

e = cast(T,day~month,mean,subset=variable=='ozone')
e # ozone variable에 대해서만 처리

f = cast(T,month~variable,range)
f # min(_X1), max(_X2)를 보여줌


## sqldf 활용
install.packages('sqldf')
library(sqldf)
data(iris)
sqldf('select*from iris') # iris데이터에서 전부 선택
sqldf('select*from iris limit 5') # 5줄만 선택
sqldf('select count(*) from iris where species like "se%"') # spscies 컬럼에서 se로 시작되는 데이터개수


## plyr
# apply(x,margin,fun) : x에 fun을 margin 방향으로 적용 결과를 반환
# margin=1이면 행방향 2이면 열방향
a = matrix(1:6,ncol=2)
a
apply(a,1,sum)
apply(iris[,-5],2,sum)
colSums(iris[,-5])
# colSums(), colMeans(), rowSums(), rowMeans() 가능

# laaply(x,함수) : 벡터, 리스트, 데이터프레임에 함수 적용해서 리스트로 반환
x = list(1:10,c(1,3,5,7,9),c(4,5,6,7,8,9,10))
x
lapply(x,mean)

# tapply(데이터, 색인(factor), 함수) : 그룹별 처리를 위한 apply함수
tapply(iris$Sepal.Length,iris$Species,mean) # iris데이터에서 species에 따른 length의 평균
tapply(1:5, 1:5 %% 2 ==1, sum) # 각 요소 중 짝,홀에 따라 합

## 데이터 테이블
install.packages('data.table')
library(data.table)
DT = data.table(x=c('b','b','b','a','a'),v=rnorm(5))
DT    

str(cars)
CARS = as.data.table(cars)
head(CARS)

sapply(CARS,class) # 데이터 타입 확인
setkey(DT,x) # key 설정
DT
tables() # DT만 키 설정된 것 확인
DT['b'] # 키가 'b'인 데이터
DT['b',mult='first'] # 키가 'b'인 데이터 중 처음
DT['b',mult='last'] # 키가 'b'인 데이터 중 마지막
