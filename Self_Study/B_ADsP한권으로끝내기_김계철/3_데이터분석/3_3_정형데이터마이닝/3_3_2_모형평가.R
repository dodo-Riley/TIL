## infert data를 신경망 모형과 의사결정 모형을 통해 모형 평가해보기
set.seed(1234)
infert <- infert[sample(nrow(infert)),] # random suffle 
infert <- infert[,c("age","parity","induced","spontaneous","case")]
trainData <- infert[1:(nrow(infert)*0.7),]
testData <- infert[((nrow(infert)*0.7)+1):nrow(infert),]

# neural network

library(neuralnet)
net.infert <- neuralnet(case~age+parity+induced+spontaneous, data=trainData,hidden=3,
                        err.fct="ce",linear.output = FALSE,likelihood=TRUE)
n_test <- subset(testData,select=-case)
nn_pred<-compute(net.infert, n_test)
testData$net_pred <- nn_pred$net.result
head(testData)

# Decision Tree
install.packages('C50')
library(C50)
trainData$case <- factor(trainData$case)
dt.infert <- C5.0(case~age+parity+induced+spontaneous, data=trainData)
testData$dt_pred <-predict(dt.infert, testData, type="prob")[,2]
head(testData)

# ROC curve packages
install.packages("Epi")
library(Epi)

# Neural Network ROC
neural_ROC <- ROC(form=case~net_pred, data=testData, plot="ROC")

# Decision Tree ROC
dtree_ROC <- ROC(form=case~dt_pred, data=testData, plot="ROC")

## prediction()을 사용해 비교
install.packages("ROCR")
library(ROCR)
n_r <- prediction(testData$net_pred, testdata$case)
d_r <- prediction(testData$dt_pred, testdata$case)
n_p <- performance(n_r,'tpr','fpr')
d_p <- performance(d_r,'tpr','fpr')
plot(n_p,col='red')
par(new=TRUE)
plot(d_p,col='blue')
abline(a=0,b=1)

n_lift <- performance(n_r,"lift","rpp")
plot(n_lift,col="red")
abline(v=0.2)