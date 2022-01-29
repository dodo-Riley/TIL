# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 08:49:28 2021

@author: sjh73
"""

# Pandas _ Series, DataFrame

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# pandas : 2차원 정형데이터(테이블, 표, 데이터프레임)

# 기본단위 : Series
# - 1차원 자료 구조
# - 하나의 데이터 타입 허용

Series([1, 2, 3, 4])
s1 = Series([1,2,3,4])
s2 = Series([1,2,3,'4'])

s3 = Series([1,2,3,4], index = ['a','b','c','d'])
# Series([1,2,3,4], ['a','b','c','d'])도 같음

Series(s3, index=['A','B','C','D']) # 이미 INDEX가 존재하는 경우

# 색인 (INDEXING)
s1[0]   # 차원 축소 일어남 >> 스칼라값
s1[0:1] # 차원 축소 일어나지 않음 
s1[[0,3]]

s3['a']
s3[0]
s3['a':'c']    # 문자의 연속 추출은 마지막 범위 포함(숫자는 마지막 포함 안함)

s1 > 2
s1[s1>2]
s3.b     # key indexing

# 연산
s1 + 1

s4 = Series([10,20,30,40])
s5 = Series([10,20,30,40], index=['c','d','e','f'])

s1 + s4 # key가 같은 값끼리 연산 가능
s3 + s5 # key 값이 동일하지 않을 때, 다른 경우는 NAN 반환
s3.add(s5, fill_value=0) # 양쪽에 동시에 존재하지 않는 key의 경우, fill_value를 통해 0으로 처리하고 연산 수행하도록함
s3.sub(s5, fill_value=0)
s3.mul(s5, fill_value=1)
s3.div(s5, fill_value=1)


# 기본 메소드
s1.dtype      # 데이터 타입 출력
s1.index      # 인덱스 출력
s3.values     # 값 출력

s3 = s3[['c','d','a','b']]  # 색인 사용, 배치 순서 변경
s3.reindex(['c','d','a','b'])  # 이미 있는 것을 순서만 바꿀때
s3.index = [ 'A','B','C','D']  # 아예 다른 것으로 바꿀때
s3[0] = 10  # 값을 바꿀때

# DataFrame
# 2차원 자료구조 (행과 열 구조)

# 생성
d1 = {'name': ['smith', 'will'], 'sal':[900,1000]}

d2 = DataFrame(d1)
d2

d3 = DataFrame(np.arange(1,7).reshape(2,3), index = ['a','b'], columns = ['col1', 'col2', 'col3']) 
d3

# 색인(indexing)

# 컬럼 선택
d3.col1
d3['col1']

# iloc, loc
# iloc : positional indexing
# loc : label indexing

d3
d3.iloc[:,0]
d3.iloc[:,0:3]
d3.iloc[:,[0,-1]]
d3.loc[:,['col1','col3']]

# 조건색인 처리
d3.loc[d3.col1 == 1,:]

# 기본 메소드
d3.dtypes # 각 컬럼 별 데이터 타입 확인
d3.index
d3.columns
d3.values
d3.columns=['A','B','C']
d3

# 연산
d3 +10
d4 = DataFrame({'A':[10,40],'B':[20,30],'C':[30,40]}, index=['A','B'])
d5 = DataFrame({'A':[10,40],'B':[20,30]}, index=['A','B'])

d3 + d5
d3.add(d5, fill_value=0)
