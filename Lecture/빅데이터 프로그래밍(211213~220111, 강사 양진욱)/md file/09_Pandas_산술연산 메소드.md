# 09. Pandas_산술연산 메소드

```python
import numpy as np 
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(1,17).reshape(4,4)) 
# 1이상 17미만의 값으로 array 생성, 4X4 형태로 변환

df1
#     0   1   2   3
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  13  14  15  16

dir(df1) # df1에 사용할수 있는 목록이 나옴

df1.sum() 
# 각 열을 행별로 더함
# 0    28
# 1    32
# 2    36
# 3    40
# dtype: int64

df1.sum(axis=0) 
# 행별(서로 다른 행끼리) 합, df1.sum()와 같은 결과

df1.sum(axis=1) 
# 열별(서로 다른 열끼리)
# 0    10
# 1    26
# 2    42
# 3    58
# dtype: int64

df1.iloc[:,0].sum() # df1의 모든 행, 1번째 열의 합
df1.iloc[:,0].mean() # df1의 모든 행, 1번쨰 열의 평균

df1.iloc[0,0] = np.nan # df1의 1번째행, 1번째 열의 값을 NaN으로 변경

df1.iloc[:,0].mean() 
# DF1의 모든 행, 1번째 열의 평균
# 자동으로 NaN 무시하고 연산함 > skipna = True (default) 
 
df1.iloc[:,0].isnull() # df1의 모든 행, 1번째 열에서 NaN 확인 > bool 형태로 결과

df1.iloc[:,0][df1.iloc[:,0].isnull()] = df1.iloc[:,0].mean()
# df1의 모든 행, 1번째 열에서 해당값이 NaN인 경우, 평균값으로 변경

df1[df1.isnull()] # 데이터프레임 전체에서 NaN 값 확인 
df1[df1.notnull()]

df1.iloc[:,0].var() # 분산 
df1.iloc[:,0].std() # 표준편차 
df1.iloc[:,0].min() 
df1.iloc[:,0].max() 
df1.iloc[:,0].median() # 중앙값

(df1.iloc[:,0] >= 10).sum() # 조건에 맞는 개수 확인
```