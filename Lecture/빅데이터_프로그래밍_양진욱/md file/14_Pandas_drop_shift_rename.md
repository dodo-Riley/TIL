# 14. Pandas_drop, shift, rename

# 14.1. drop

> 특정 행이나 컬럼을 제거한다. index나 column의 이름으로 전달 가능하다.
> 

```python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

emp = pd.read_csv("./data/emp.csv")
emp
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000

emp['ename'] == 'scott' # 'ename' 컬럼 중 'scott'인지 아닌지
emp.loc[emp['ename'] == 'scott'] # 'ename' 컬럼 중 'scott'인 행
emp.loc[emp['ename'] == 'scott',:] # 'ename' 컬럼 중 'scott'인 행, 모든 열
emp.loc[~(emp['ename'] == 'scott'),:] # 'ename' 컬럼 중 'scott'이 아닌 행, 모든 열

emp.drop(4, axis=0) # 행기준, 4번째 idx 제외
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 5      6   king      20  4000

emp.drop('sal', axis=1) # 열 기준, 'sal' column을 제거
#    empno  ename  deptno
# 0      1  smith      10
# 1      2  allen      10
# 2      3   ford      20
# 3      4  grace      10
# 4      5  scott      30
# 5      6   king      20

emp.drop(['ename','deptno'], axis=1) # 행 기준, 'ename'과 'deptno' 열 제거
#    empno   sal
# 0      1  4000
# 1      2  4500
# 2      3  4300
# 3      4  4200
# 4      5  4100
# 5      6  4000
```

# 14.2. shift

> 행 또는 열을 이동시킨다. 전일 대비 증감률과 같은 결과를 얻을 수 있다.
> 

```python
emp
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000

emp['sal'].shift() 
# default : 1행, axis=0 기준, 'sal' 열을 한 행씩 이동
# 0       NaN
# 1    4000.0
# 2    4500.0
# 3    4300.0
# 4    4200.0
# 5    4100.0
# Name: sal, dtype: float64

s1 = Series([3000,3500,4200,2800,3600], index=['2021/01/01','2021/01/02','2021/01/03','2021/01/03','2021/01/05'])
s1
# 2021/01/01    3000
# 2021/01/02    3500
# 2021/01/03    4200
# 2021/01/03    2800
# 2021/01/05    3600
# dtype: int64

s2 = s1.shift() # s1 Series를 한 행씩 이동
s2
# 2021/01/01       NaN
# 2021/01/02    3000.0
# 2021/01/03    3500.0
# 2021/01/03    4200.0
# 2021/01/05    2800.0
# dtype: float64

((s1-s2)/s1)*100 # s1 기준으로 s2의 증감률 결과 반환
# 2021/01/01          NaN
# 2021/01/02    14.285714
# 2021/01/03    16.666667
# 2021/01/03   -50.000000
# 2021/01/05    22.222222
# dtype: float64
```

# 14.3. rename

> 행과 컬럼의 name을 변경한다.
> 

```python
emp
emp.columns = ['emptno','ename','deptno','salary']
# emp의 컬럼명을 해당 값으로 변경
#    emptno  ename  deptno  salary
# 0       1  smith      10    4000
# 1       2  allen      10    4500
# 2       3   ford      20    4300
# 3       4  grace      10    4200
# 4       5  scott      30    4100
# 5       6   king      20    4000

emp.rename({0:'a',2:'b'}, axis=0)
# 인덱스명 변경
#    emptno  ename  deptno  salary
# a       1  smith      10    4000
# 1       2  allen      10    4500
# b       3   ford      20    4300
# 3       4  grace      10    4200
# 4       5  scott      30    4100
# 5       6   king      20    4000

emp.rename({'salary':'sal','deptno':'dept_no'}, axis=1)
# column명 변경
#    emptno  ename  dept_no   sal
# 0       1  smith       10  4000
# 1       2  allen       10  4500
# 2       3   ford       20  4300
# 3       4  grace       10  4200
# 4       5  scott       30  4100
# 5       6   king       20  4000  

emp_re = emp.set_index('ename') 
# 'ename' 열을 index로 설정
#        emptno  deptno  salary
# ename                        
# smith       1      10    4000
# allen       2      10    4500
# ford        3      20    4300
# grace       4      10    4200
# scott       5      30    4100
# king        6      20    4000

emp_up = emp_re.rename({'scott':'SCOTT'}, axis=0) 
# scott을 대문자로 변경
#        emptno  deptno  salary
# ename                        
# smith       1      10    4000
# allen       2      10    4500
# ford        3      20    4300
# grace       4      10    4200
# SCOTT       5      30    4100
# king        6      20    4000

emp.set_index('ename').rename({'scott':'SCOTT'})
# method chaining을 통해 한 줄로 작성
```