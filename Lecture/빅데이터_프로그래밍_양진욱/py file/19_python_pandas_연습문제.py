# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:13:22 2021

@author: sjh73
"""

# 1번
run my_modules
import matplotlib.pyplot as plt

df1 = pd.read_csv('./data/cancer_test.csv')
df1.columns
df1.dtypes
df1.head()
df1.info()
df1.describe()

# 1.1) radius_mean, texture_mean, texture_se, smoothness_se에 대해 na인 행 제거한 후, 총 행의 수 반환
df1['radius_mean'].isnull().sum() # radius_mean 열에서 na인 값의 개수
df1['texture_mean'].isnull().sum() # texture_mean 열에서 na인 값의 개수
df1['texture_se'].isnull().sum() # texture_se 열에서 na인 값의 개수
df1['smoothness_se'].isnull().sum() # smoothness_se 열에서 na인 값의 개수

vbool = df1['radius_mean'].isnull() & df1['texture_mean'].isnull() & df1['texture_se'].isnull() & df1['smoothness_se'].isnull()
vbool.sum() # 4개가 모두 na인 행의 개수

df1.loc[vbool,:] # 4개가 모두 na인 행 색인

df1.shape      # df1의 형태
df1.shape[0]   # df1의 행 수
df1.shape[1]   # df1의 열 수
df1.shape[0]-vbool.sum() # not null 개수

nrow = df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how ='all').shape[0]
print(nrow)   # 답

# 1.2) concavity_mean의 standard scailing(표준화) 후, 결과가 0.1 이상인 값의 개수 출력
# standard scailing : (값-평균)/표준편차
# minmax scailing = (값-최소)/(최대-최소)
df1.columns
vscale = (df1['concavity_mean']-df1['concavity_mean'].mean())/df1['concavity_mean'].std()
(vscale>0.1).sum()  # 답

# 1.3) 이상치 건 수 확인
# texture_Se의 상위 10% 값(na를 제외한 건수의 10%)를 이상치로 가정
# 10%를 제외한 값의 최대값으로 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력

df1['texture_se'].dropna().shape[0]
nx = int(np.trunc(df1['texture_se'].dropna().shape[0] * 0.1))
vrank = df1['texture_se'].rank(ascending = False, method='first')  # rank 함수 따로 정리할 것.
# vrank_ = df1['texture_se'].sort_values(ascending = False) 그냥 sort써서 하면 안되나...? 확인해보기
df1.loc[vrank>nx, 'texture_se']  # 정상치 데이터
df1.loc[vrank<=nx, 'texture_se']  # 이상치 데이터
vmax = df1.loc[vrank>nx, 'texture_se'].max() # 10%를 제외한 값의 최대값
df1.loc[vrank<=nx, 'texture_se'] = vmax # 이상치를 원하는 값으로 변경
mean_ = df1['texture_se'].mean()
round(mean_,2)
# print('%0.2f' % mean_) 쳐도 나옴

# 1.4) symmetry_mean의 결측치를 최소값으로 수정한 후 평균을 소수점 둘째자리로 반올림해서 출력
df1['symmetry_mean'].min() # '-'가 존재해서 제대로 안나옴

from numpy import nan as NA

df2 = df1['symmetry_mean'].replace(['-','.','pass'], NA)   # 뭐있는지 확인 언제하냐... > for문써서 바꿔볼 것
df3 = df2.astype('float')
df3.min()
df4 = df3.fillna(df3.min())
print(round(df4.mean(),2))
