## 시계열 자료 예시
Nile
plot(Nile) # 비계절성을 띠는 데이터 확인 가능, 정상성 만족하지 않음
Nile.diff1 = diff(Nile, differences=1)
plot(Nile.diff1)# 1차 차분 결과 역시 평균이 일정하지 않음
Nile.diff2 = diff(Nile, differences = 2)
plot(Nile.diff2)# 2차 차분한 결과 어느정도 정상성을 만족

## 모형결정 및 예측
acf(Nile.diff2,lag.max=20,plot=FALSE)
acf(Nile.diff2,lag.max=20)

pacf(Nile.diff2,lag.max=20, plot=FALSE)
pacf(Nile.diff2,lag.max=20)

install.packages('forecast')
library(forecast)
auto.arima(Nile)

Nile.arima = arima(Nile, order=c(1,1,1))
Nile.arima
Nile.forecast = forecast(Nile.arima,h=50)
Nile.forecast
plot(Nile.forecast)

## 계절요인을 가지는 데이터
ldeaths
plot(ldeaths)

## decompose()
ldeaths.decompose = decompose(ldeaths)
ldeaths.decompose$seasonal
plot(ldeaths.decompose)

## 계절성 요인 제거
ldeaths.decompose.adj = ldeaths-ldeaths.decompose$seasonal
plot(ldeaths.decompose.adj)
