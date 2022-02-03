# 07. Pandas_시리즈, 데이터프레임

> Pandas는 2차원 정형데이터(테이블, 표, 데이터프레임)를 다룸
> 

# 1. Series

> 1차원 자료 구조로 pandas의 기본 단위.
> 

```python
import numpy as np 
import pandas as pd 
from pandas import Series, DataFrame

Series([1, 2, 3, 4]) 
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64

s1 = Series([1,2,3,4])  # 데이터 타입이 int64(정수)
s2 = Series([1,2,3,'4'])  # 데이터 타입이 object(문자열 또는 복합형)

s3 = Series([1,2,3,4], index = ['a','b','c','d']) 
s3
# a    1
# b    2
# c    3
# d    4
# dtype: int64
# Series([1,2,3,4], ['a','b','c','d'])도 같음

s3.index=['A','B','C','D'])
s3
# A    1
# B    2
# C    3
# D    4
# dtype: int64
# 이미 index가 존재하는 경우, 대체
```

- 색인 (indexing)
    
    ```python
    s1[0] # 1, 차원 축소 일어남 >> 스칼라값 
    s1[0:1] 
    # 0    1
    # dtype: int64
    # 차원 축소 일어나지 않음 
    
    s1[[0,3]]
    # 0    1
    # 3    4
    # dtype: int64
     
    s3['A'] # 1
    s3[0]   # 1
    s3['A':'C'] 
    # A    1
    # B    2
    # C    3
    # dtype: int64
    # 문자의 연속 추출은 마지막 범위 포함(숫자는 마지막 포함 안함)
    
    s1 > 2
    # 0    False
    # 1    False
    # 2     True
    # 3     True
    # dtype: bool
    
    s1[s1>2]
    # 2    3
    # 3    4
    # dtype: int64
    
    s3.B # 2, key indexing
    ```
    

- 연산
    
    ```python
    s1 + 1
    # 0    2
    # 1    3
    # 2    4
    # 3    5
    # dtype: int64
    # 각각에 1을 더함
    
    s4 = Series([10,20,30,40]) 
    s5 = Series([10,20,30,40], index=[‘c’,‘d’,‘e’,‘f’])
    
    s1 + s4 
    # 0    11
    # 1    22
    # 2    33
    # 3    44
    # dtype: int64
    # key가 같은 값끼리 연산 가능
     
    s3 + s5
    # A   NaN
    # B   NaN
    # C   NaN
    # D   NaN
    # c   NaN
    # d   NaN
    # e   NaN
    # f   NaN
    # dtype: float64
    # key 값이 동일하지 않을 때, 다른 경우는 NAN 반환 
    
    # 양쪽에 동시에 존재하지 않는 key의 경우, fill_value를 통해 해당 값으로 처리하고 연산 수행하도록함
    s3.add(s5, fill_value=0) # 더하기 
    s3.sub(s5, fill_value=0) # 빼기
    s3.mul(s5, fill_value=1) # 곱하기
    s3.div(s5, fill_value=1) # 나누기
    ```
    

- 기본 메소드
    
    ```python
    s1.dtype # 데이터 타입 출력 
    s1.index # 인덱스 출력 
    s3.values # 값 출력
    s3 = s3[['C','D','A','B']] # 색인 사용, 배치 순서 변경 
    s3.reindex(['C','D','A','B']) # 이미 있는 것을 순서만 바꿀때 
    s3.index = ['a','b','c','d'] # 아예 다른 것으로 바꿀때 
    s3[0] = 10 # 값을 바꿀때
    ```
    

# 2. DataFrame

> 2차원 자료구조 (행과 열 구조)
> 

- 생성
    
    ```python
    d1 = {'name': ['smith', 'will'], 'sal':[900,1000]}
    d2 = DataFrame(d1) 
    d2
    #     name   sal
    # 0  smith   900
    # 1   will  1000
    
    d3 = DataFrame(np.arange(1,7).reshape(2,3), index = ['a','b'], columns = ['col1', 'col2', 'col3']) 
    d3
    #    col1  col2  col3
    # a     1     2     3
    # b     4     5     6
    ```
    
- 색인(indexing)
    - 컬럼 선택
        
        ```python
        d3.col1 
        d3['col1']
        ```
        
    
    - `iloc`, `loc`
        
        ```python
        # iloc : interger location, 행이나 열의 순서를 나타내는 정수로 값 추출
        # loc : 칼럼명이나 특정 조건식을 써줌으로써 값 추출
        
        d3.iloc[:,0] 
        d3.iloc[:,0:3] 
        d3.iloc[:,[0,-1]] 
        d3.loc[:,['col1','col3']]
        ```
        
    
    - 조건색인 처리
        
        ```python
        d3.loc[d3.col1 == 1, :]
        #   col1  col2  col3
        #a     1     2     3
        ```
        

- 기본 메소드
    
    ```python
    d3.dtypes # 각 컬럼 별 데이터 타입 확인 
    d3.index  # 인덱스만 추출
    d3.columns # 열 이름만 추출
    d3.values  # 값만 추출
    d3.columns=[‘A’,‘B’,‘C’] # 열 이름 변경 
    ```
    

- 연산
    
    ```python
    d3 + 10  # 모든 요소에 10 더함
    
    d4 = DataFrame({'A':[10,40],'B':[20,30],'C':[30,40]}, index=['A','B']) 
    d5 = DataFrame({'A':[10,40],'B':[20,30]}, index=['A','B'])
    
    d3 + d5 
    #     A   B   C
    # A NaN NaN NaN
    # B NaN NaN NaN
    # a NaN NaN NaN
    # b NaN NaN NaN
    
    d3.add(d5, fill_value=0)
    #       A     B    C
    # A  10.0  20.0  NaN
    # B  40.0  30.0  NaN
    # a   1.0   2.0  3.0
    # b   4.0   5.0  6.0
    ```