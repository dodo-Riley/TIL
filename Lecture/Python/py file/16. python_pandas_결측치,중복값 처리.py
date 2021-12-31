# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:55:41 2021

@author: sjh73
"""

# 결측치, 중복값 제거

# 결측치(Na) 처리
# 숫자형 NA(float type), 문자형 NA

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([1,2,3,np.nan])
s2 = Series(['a','b','c',np.nan])

# 1. NA 수정
s1.mean() # nan을 skip하고 나머지로 평균 구한 결과를 반환(default)
s1.fillna(0) # nan을 0으로 대체
s2.replace(np.nan, 'a') # nan을 'a'로 대체

# 조건 색인을 해서 na 처리 가능
s1.isnull() 
s1[s1.isnull()] = 0

# 2. NA로의 수정

s3 = Series(['서울','.','대전','.','대구','.','부산'])
s4 = s3.replace('.',np.nan)

# 3. NA를 이전 값/ 이후 값 수정
s4.fillna(method = 'ffill') 
s4.ffill()  # 변수명.ffill() : NA를 앞에 있는 값으로 치환
s4.fillna(method = 'bfill')  # 뒤에 있는 값으로 치환

# 4. NA를 갖는 행, 열 제거
df1 = DataFrame(np.arange(1,17).reshape(4,4), columns = list('ABCD'))
df1.iloc[0,0] = np.nan
df1.iloc[1,[0,1]] = np.nan
df1.iloc[2,[0,1,2]] = np.nan
df1.iloc[3,:] = np.nan

df1.dropna()  # NaN이 존재하는 행 제거
df1.dropna(how='any') # NaN이 하나라도 존재하는 행 제거
df1.dropna(how='all') # 모든 요소가 NaN인 행 제거
df1.dropna(thresh=2)  # NaN이 아닌 값이 최소 2개 이상이면 제거 X
df1.dropna(axis=1, how='all') # 특정 컬럼이 모두 na로만 구성되어 있으면 해당 컬럼 제거
df1.dropna(subset=['C']) # 'C' 컬럼에 na가 있는 행 제거

# 중복값 처리
s5 = Series([1,1,2,3,4])
s5.unique() # 유일한 값 확인, array
s5.duplicated() # 중복된 값 확인, bool
s5.drop_duplicates() # 중복된 값 제거, Series

df4 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40]})
df4.drop_duplicates()

df5 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40], 'C':[100,200,300,400]})
df5.drop_duplicates() # 모든 컬럼의 값이 일치하는 행을 제거

df5.drop_duplicates(subset=['A','B']) # 'A','B' 컬럼에서 값이 일치하는 행 제거
df5.drop_duplicates(subset=['A','B'], keep='last') # 중복되는 것 중에서 마지막 것 살림
df5.drop_duplicates(subset=['A','B'], keep='first') # 중복되는 것 중에서 처음 것 살림



