## 로지스틱 회귀
# 단순선형회귀식 추정
x = c(27.2,27.7,28.3,28.4,29.9) # 온도
male = c(2,17,26,19,27) # 수컷 수
female = c(25,7,4,8,1) # 암컷 수
total = male+female
pmale = male/total
z = lm(pmale~x) # 회귀분석(종속변수~독립변수)
summary(z)
p = coefficients(z)[1]+coefficients(z)[2]*x
p

# 로짓변환된 값을 종속변수로 단순 선형 회귀식 추정
logit = log(pmale/(1-pmale))
z1 = lm(logit~x)
summary(z1)
logit2 = coefficients(z1)[1]+coefficients(z1)[2]*x
rmalehat = exp(logit2)/(1+exp(logit2))
rmalehat

# 최대우도추정법을 사용하여 회귀방정식 추정
logit = glm(pmale~x,family="binomial", weight=total)
summary(logit)
exp(-61.3183)*exp(2.2111*27)
exp(-61.3183)*exp(2.2111*28)

# iris 데이터를 활용한 로지스틱 회귀분석
colnames(iris) = tolower(colnames(iris))
a = subset(iris,species=='setosa'|species=='versicolor')
a$species = factor(a$species)
b = glm(species~sepal.length,data=a,family=binomial)
summary(b)
coef(b)
cdplot(species~sepal.length,data=a)

# 이항변수 vs를 반응변수로, mpg와 am을 예측변수로 하는 로지스틱 회귀모형 추정
glm.vs = glm(vs~mpg+am,data=mtcars, family="binomial")
summary(glm.vs)

## 인공신경망
colnames(iris) = tolower(colnames(iris))
install.packages("nnet")
library(nnet)
data = iris
Scale = data.frame(lapply(data[,1:4], function(x) scale(x)))
Scale$species = data$species
index = sample(1:nrow(Scale), round(0.75*nrow(Scale)), replace=FALSE)
train = Scale[index,]
test = Scale[-index,]
model = nnet(species~.,size=2,decay=5e-04,data=train)
summary(model)
predict.model = predict(model,test[,1:4],type="class")
predict.model
actual = test$species
confusion.matrix = table(actual, predict.model)
confusion.matrix
sum(predict.model==actual)/NROW(predict.model)

## 의사결정나무
colnames(iris) = tolower(colnames(iris))
library('rpart')
k = rpart(species~.,data=iris)
k
plot(k,compress=T,margin=.3)
text(k,cex=1.0)

install.packages('rpart.plot')
library('rpart.plot')
prp(k,type=4,extra=2,digits=3)

head(predict(k,newdata=iris,type='class'))
printcp(k)
plotcp(k)
install.packages('caret')
library(caret)
install.packages('e1071')
library(e1071)
rpartpred = predict(k,iris,type='class')
confusionMatrix(rpartpred,iris$species)

## 앙상블

# 배깅
install.packages('adabag')
library(adabag)
library(rpart)
data(iris)
#test 데이터 생성 : 배깅은 이 test data를 모집단으로 생각하고 평균예측모형을 구하기 때문에 분산을 줄이고 예측력을 향상시킬 수 있다.
set.seed(1)
train <- c(sample(1:50,25),sample(51:100,25),sample(101:150,25))

#bagging 모델링 적용
iris.bagging<-bagging(Species~.,data=iris[train,], mfinal=10,control=rpart.control(maxdepth=1))
iris.bagging
#mfinal : tree 반복생성 횟수, control은 tree분석의 "rpart.control" 적용

#iris.bagging 결과 : 의사결정 나무 결과 10개, vote 결과, 최종 결정 결과, bootstrap sample 10개, 변수의 중요도
#tree를 호출하면 각기 다른 tree가 생성됨을 확인 할 수 있다.
iris.bagging$tree[[1]]
iris.bagging$tree[[2]]

#test data에서 랜덤 복원추출(Random Sampling) 한 bootstrap 자료 확인 _ 복원추출이라서 하나의 값이 여러번 뽑힌 것을 확인 할 수 있다.
sample1<-iris.bagging$samples[,1] 
sample2<-iris.bagging$samples[,2]
table(sample1)
table(sample2)

#voting에 의한 최종 결정 결과 확인
iris.bagging$class           

#변수의 중요도 출력
iris.bagging$importance      
barplot(iris.bagging$importance[order(iris.bagging$importance, decreasing=TRUE)],ylim=c(0,100), main="Variables Relative Importance", col="blue")

#배깅 모형의 정확도 계산하기
Table <- table(iris.bagging$class, iris$Species[train], dnn=c("Predicted Class", "Observed Class"))
accuracy <- sum(diag(Table))/sum(Table) 

# 부스팅
library(adabag)
set.seed(1)
train <- c(sample(1:50,25),sample(51:100,25), sample(101:150,25))
iris.adaboost <- boosting(Species~.,data=iris[train,],
                          mfinal=10,control=rpart.control(maxdepth=1))
iris.adaboost

#의사결정나무 10개, weights 10개, vote로 인한 최종결정(class), 변수의 중요도(importance)
iris.adaboost$importance

#bagging의 결과와 약간 다르다.
barplot(iris.adaboost$importance[order(iris.adaboost$importance,decreasing=TRUE)],ylim=c(0,100), main="Variable relative importance")

#부스팅 모형의 정확도 계산하기
Table <- table(iris.adaboost$class, iris$Species[train], dnn=c("Predicted Class", "Observed Class"))
accuracy <- sum(diag(Table))/sum(Table) 

#배깅과 정확도 일치한다.

# 랜덤포레스트
install.packages('randomForest')
library(randomForest)
library(rpart)
data(stagec)
stagec3 <- stagec[complete.cases(stagec),]
set.seed(1234)
ind <- sample(2, nrow(stagec3), replace = TRUE, prob=c(0.7, 0.3))
trainData<-stagec3[ind==1, ] #n=102개
testData<-stagec3[ind==2, ] #n=32개
rf <- randomForest(ploidy~., data=trainData, ntree=100, proximity=TRUE)
table(predict(rf), trainData$ploidy)
print(rf)
plot(rf)
importance(rf)
varImpPlot(rf)

rf.pred <- prdict(rf, newdata=testData)
table(rf.pred, testData$ploidy)
plot(margin(rf))

set.seed(1234)
cf <- cforest(ploidy ~ ., data=trainData)
cf.pred <- predict(cf, newdata=testData, OOB=TRUE, type="response")

# SVM
library(e1071)
s = sample(150,100)
col = c('Petal.Length','Petal.Width','Species')
iris_train = iris[s,col]
iris_test = iris[-s,col]
iris_svm = svm(Species~.,data=iris_train,cost=1,kernel='linear')
plot(iris_svm,iris_train[,col])
p = predict(iris_svm,iris_test[,col],type='class')
plot(p)
table(p,iris_test[,3])

# naive bayes
library(e1071)
data(iris)
colnames(iris) = tolower(colnames(iris))
m = naiveBayes(species~.,data=iris)
m
table(predict(m, iris[,-5]),iris[,5],dnn=list('predicted','actual'))

# KNN
data(iris)
install.packages('DMwR')
library(DMwR)
