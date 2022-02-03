# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 15:19:02 2021

@author: sjh73
"""

# 22. scailing
# 변수 스케일링(표준화)

# 설명변수의 서로 다른 범위에 있는 것을 동일한 범주 내 비교하기 위한 작업 
# - 거리 기반 모델
#   ex) knn, clustering, PCA, SVM, NN 모델 등에 필요
# - 각 설명변수의 중요도를 정확하게 비교하기 위해 요구됨 
# - 이상치에 덜 민감하게 조정

# 스케일링의 종류 

# 1) Standard Scailing
# - 평균을 0, 표준편차 1 로 맞추는 작업

# 2) MinMax Scailing
# - 최소값 0, 최대값 1 로 맞추는 작업

# 3) Robust Scailing
# - 중앙값 0, IQR 1 로 맞추는 작업


# scailing module 불러오기
from sklearn.preprocessing import StandardScaler as standard
from sklearn.preprocessing import MinMaxScaler as minmax

# iris data loading
from sklearn.datasets import load_iris

iris_x = load_iris()['data']
iris_y = load_iris()['target']

# 1. standard scailing

# 직접 계산 : (x-x_bar)/sigma

df1 = (iris_x-iris_x.mean(axis=0))/iris_x.std(axis=0)
df1.min()
df1.max()

# 함수 사용
m_sc = standard()
m_sc.fit(iris_x)  # fit() : 데이터를 모델에 적합하게 해주는 함수
m_sc.transform(iris_x) # transform : 변환

# 2. minmax scailing

# 직접 계산 : (x-x.min())/(x.max()-x.min())
df2 = (iris_x-iris_x.min(0))/(iris_x.max(0)-iris_x.min(0))
df2.max()
df2.min()

# 함수 사용
mm = minmax()
mm.fit(iris_x)
df2 = mm.transform(iris_x)

df2.max()
df2.min()

# train/test로 분리되어진 데이터를 표준화
from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y)

# train_x와 test_x 동일한 기준으로 스케일링 (good)
mm_2 = minmax()
mm_2.fit(train_x)

train_mm = mm_2.transform(train_x)
test_mm = mm_2.transform(test_x)

train_mm.min(0)
train_mm.max(0)   # 1과 0 나옴

test_mm.min(0)  
test_mm.max(0)    # 1, 0 안나옴

# train_x와 test_x 다른 기준으로 스케일링 (bad)
mm_2 = minmax()
mm_3 = minmax()

mm_2.fit(train_x)
mm_3.fit(test_x)

train_mm_2 = mm_2.transform(train_x)
test_mm_3 = mm_3.transform(test_x)

train_mm_2.min()
train_mm_2.max()

test_mm_3.min()
test_mm_3.max()
