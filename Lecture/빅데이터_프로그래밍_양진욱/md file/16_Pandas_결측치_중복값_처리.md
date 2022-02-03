# 16. Pandas_결측치와 중복값 처리

# 16.1. 결측치 처리

- NA 수정
    
    ```python
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    
    s1 = Series([1,2,3,np.nan])
    s2 = Series(['a','b','c',np.nan])
    
    s1.mean() # NaN을 skip하고 나머지로 평균 구한 결과를 반환(default)
    
    s1.fillna(0) # NaN을 0으로 대체
    s2.replace(np.nan, 'a') # nan을 'a'로 대체
    s1[s1.isnull()] = 0 # s1에서 NaN인 값만 0으로 대체
    ```
    

- NA로의 수정
    
    ```python
    s3 = Series(['서울','.','대전','.','대구','.','부산'])
    s4 = s3.replace('.',np.nan) # s3에서 '.'을 NaN으로 대체
    ```
    

- NA를 이전 값/ 이후 값 수정
    
    ```python
    s4.fillna(method = 'ffill') # NaN를 이전 값으로 대체
    s4.ffill()  # NaN를 이전 값으로 대체
    s4.fillna(method = 'bfill')  # NaN를 이후 값으로 대체
    ```
    

- NA를 갖는 행, 열 제거
    
    ```python
    df1 = DataFrame(np.arange(1,17).reshape(4,4), columns = list('ABCD'))
    #     A   B   C   D
    # 0   1   2   3   4
    # 1   5   6   7   8
    # 2   9  10  11  12
    # 3  13  14  15  16
    
    df1.iloc[0,0] = np.nan       # df1의 1행, 1열 값을 NaN으로 대체
    df1.iloc[1,[0,1]] = np.nan   # df1의 2행, 1열과 2열 값을 NaN으로 대체
    df1.iloc[2,[0,1,2]] = np.nan # df1의 3행, 1열부터 3열까지 값을 NaN으로 대체
    df1.iloc[3,:] = np.nan       # df1의 4행의 모든 값을 NaN으로 대체
    #     A    B    C     D
    # 0 NaN  2.0  3.0   4.0
    # 1 NaN  NaN  7.0   8.0
    # 2 NaN  NaN  NaN  12.0
    # 3 NaN  NaN  NaN   NaN
    
    df1.dropna()  # NaN이 존재하는 행 제거
    df1.dropna(how='any') # NaN이 하나라도 존재하는 행 제거
    df1.dropna(how='all') # 모든 요소가 NaN인 행 제거
    df1.dropna(thresh=2)  # NaN이 2개 초과인 행 제거
    df1.dropna(axis=1, how='all') # 특정 컬럼이 모두 NaN로만 구성되어 있으면 해당 컬럼 제거
    df1.dropna(subset=['C']) # 'C' 컬럼에 NaN가 있는 행 제거
    ```
    

# 16.2. 중복값 처리

```python
s5 = Series([1,1,2,3,4])
s5.unique() 
# 유일한 값 확인, array
# array([1, 2, 3, 4], dtype=int64)

s5.duplicated() 
# 중복된 값 확인, bool
# 0    False
# 1     True
# 2    False
# 3    False
# 4    False
# dtype: bool

s5.drop_duplicates() 
# 중복된 값 제거, Series
# 0    1
# 2    2
# 3    3
# 4    4
# dtype: int64

df4 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40]})
df4.drop_duplicates()
# A열과 B열 동시에 중복되는 값을 가지는 행 제거
#    A   B
# 0  1  10
# 2  3  30
# 3  4  40

df5 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40], 'C':[100,200,300,400]})
df5.drop_duplicates() 
# 모든 컬럼의 값이 일치하는 행을 제거하므로 제거되는 행이 없음
#    A   B    C
# 0  1  10  100
# 1  1  10  200
# 2  3  30  300
# 3  4  40  400

df5.drop_duplicates(subset=['A','B']) 
# 'A','B' 컬럼에서 값이 일치하는 행 제거
#    A   B    C
# 0  1  10  100
# 2  3  30  300
# 3  4  40  400

df5.drop_duplicates(subset=['A','B'], keep='last') 
# 중복되는 것 중에서 마지막 것 살림
#    A   B    C
# 1  1  10  200
# 2  3  30  300
# 3  4  40  400

df5.drop_duplicates(subset=['A','B'], keep='first') 
# 중복되는 것 중에서 처음 것 살림
#    A   B    C
# 0  1  10  100
# 2  3  30  300
# 3  4  40  400
```