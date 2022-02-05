## 상관계수의 유의성 검정
a=c(1,2,3,4,5);b=c(1,0,5,7,9)
cor.test(a,b,method='pearson')

## 다차원척도 그래프
data("eurodist")
print(eurodist)
loc = cmdscale(eurodist)
loc
x = loc[,1];y=loc[,2]
plot(x,y,type='n',main='eurodis')
text(x,y,rownames(loc),cex=.8,col='red')
abline(v=0,h=0)

## 주성분분석 
library(datasets)
data("USArrests")
head(USArrests)
fit = prcomp(USArrests,scale=TRUE) # 주성분분석함수, scale=True는 표준화의미미
summary(fit)
biplot(fit)
