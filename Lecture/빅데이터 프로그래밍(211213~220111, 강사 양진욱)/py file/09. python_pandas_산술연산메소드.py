# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:06:12 2021

@author: sjh73
"""

import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(1,17).reshape(4,4))
df1

dir(df1) # df1에 사용할수 있는 목록이 나옴

df1.sum()
df1.sum(axis=0) # 행별(서로 다른 행끼리)
df1.sum(axis=1) # 열별(서로 다른 열끼리)

df1.iloc[:,0].sum()
df1.iloc[:,0].mean()

df1.iloc[0,0] = np.nan
df1.iloc[:,0].mean()
# skipna = True (default) 자동으로 NaN 무시하고 연산

# 평균값(최대 또는 최소) 대치
df1.iloc[:,0].mean()
df1.iloc[:,0].isnull()

df1.iloc[:,0][df1.iloc[:,0].isnull()] = df1.iloc[:,0].mean()

df1[df1.isnull()] # 데이터프레임 전체에서 NaN 값 확인
df1[df1.notnull()]

df1.iloc[:,0].var()  # 분산
df1.iloc[:,0].std()  # 표준편차
df1.iloc[:,0].min()
df1.iloc[:,0].max()
df1.iloc[:,0].median()  # 중앙값

(df1.iloc[:,0] >= 10).sum()  # 조건에 맞는 개수 확인
