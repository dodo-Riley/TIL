## 데이터 기초 통계
data(iris) # 데이터 불러오기
head(iris) # 데이터 처음부터 6줄 확인 
str(iris) # 데이터 구조 파악
summary(iris) # 데이터 기초 통계량 확인
cov(iris[,1:4]) # 변수 간 공분산 확인
cor(iris[,1:4]) # 변수 간 상관계수 확인


## 결측값 처리
y = c(1,2,3,NA)
is.na(y) # 결측값 여부 확인

# 특정값을 결측값으로 대체
data(iris)
iris[iris$Petal.Width==0.2,'Petal.Width'] = NA
is.na(iris$Petal.Width)

# 결측값 제외하고 수행
x = c(1,2,NA,3)
mean(x)
mean(x,na.rm=TRUE)

# 결측값을 포함하는 행 찾기
data("french_fries")
french_fries[!complete.cases(french_fries),]

# amelia 패키지를 이용한 결측값 대치
install.packages('Amelia')
library(Amelia)
data(freetrade)
head(freetrade)
a.out = amelia(freetrade, m=5, ts='year', cs='country') 
# m=가상의 데이터셋을 몇 개 만들지, ts=시계열정보(time series),cs=분석에 포함될 변수(cross sectional)

# 3번째의 imputation 데이터셋을 적용해 tariff 변수를 히스토그램 그리기
hist(a.out$imputations[[3]]$tariff, col='grey', border='white')

missmap(a.out)# 결측값을 처리하기 전의 그래프
freetrade$tariff = a.out$imputations[[5]]$tariff # imputation 데이터셋 중 5번째 데이터셋으로 대치
missmap(freetrade) # 결측값 처리 후 그래프


## R의 결측값 처리 정리
is.na() # NA값을 조사해 논리값으로 반환(NA=TRUE)
complete.cases() # NA값을 조사해 논리값으로 반환(NA=FALSE)
iris[iris$sepal.length==4.0] = NA # 특정값을 NA 처리

# 데이터프레임에서 결측값만 선택 또는 삭제
iris_na = iris
iris_na[c(10,20,30),3] = NA # iris_na 3열의 10,20,30행을 NA처리
iris_na[!complete.cases(iris_na),] # NA가 포함된 행만 추출
iris_na[complete.cases(iris_na),] # NA가 없는 행만 추출

na.omit() # NA가 있는 행 전체 삭제
na.rm=TRUE # mean, range, sd 등 수치형 변수함수 안에 사용하는 인자로 NA값이 있으면 제외하고 수행하도록 함


## 이상값 검색
install.packages('outliers')
library(outliers)
set.seed(1234) # 같은 값이 추출되도록 고정
y=rnorm(100) # 정규분포에서 난수 생성
outlier(y) # 평균과 가장 차이가 많이 나는 값 출력
outlier(y,opposite=TRUE) # 평균과 반대 방향으로 가장 차이가 많이 나는 값 출력
dim(y)=c(20,5) # y의 행,열 지정해서 행렬 생성
outlier(y) # 각 열의 평균과 가장 차이가 많이 나는 값을 열 별로 출력
outlier(y,opposite=TRUE) # 반대방향으로 차이가 많이나는 값을 열별로 출력
boxplot(y)
