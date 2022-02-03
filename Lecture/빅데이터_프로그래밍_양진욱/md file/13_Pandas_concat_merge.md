# 13. Pandas_concat, merge

# 13.1. concat

> 두 개의 데이터프레임을 합친다.
> 

```python
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(1,7).reshape(2,3), columns=['A','B','C'])
df2 = DataFrame(np.arange(10,61,10).reshape(2,3), columns=['A','B','C'])

pd.concat([df1,df2])  
# 행의 결합 > 기본은 세로 방향으로 합쳐짐
#     A   B   C
# 0   1   2   3
# 1   4   5   6
# 0  10  20  30
# 1  40  50  60

pd.concat([df1,df2],axis=0)   
# 행의 결합 > 세로 방향으로 합쳐짐, default

pd.concat([df1,df2],axis=1)   
# 열의 결합 > 가로 방향으로 합쳐짐
#    A  B  C   A   B   C
# 0  1  2  3  10  20  30
# 1  4  5  6  40  50  60

pd.concat([df1,df2], ignore_index=True)  
# 합칠 때, 기존 인덱스 무시하고 순차적으로 번호 부여
#     A   B   C
# 0   1   2   3
# 1   4   5   6
# 2  10  20  30
# 3  40  50  60
```

# 13.2. merge

> 서로 분리되어 있는 데이터 프레임을 하나의 데이터 프레임으로 합친다.
> 

- 참조 조건을 활용해 연관된 두 데이터를 병합한다.
- 등가 조건만을 사용한다.

```python
emp = pd.read_csv('./data/emp.csv')
#emp
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000

df_dept = DataFrame({'deptno':[10,20,30],'dname':['인사부','총부무','IT분석팀']})
#df_dept
#     deptno   dname
# 0      10    인사부
# 1      20    총부무
# 2      30  IT분석팀

# pd.merge(left: 'DataFrame | Series',           # 왼쪽에 붙을 자료
#          right: 'DataFrame | Series',          # 오른쪽에 붙을 자료
#          how: 'str' = 'inner',                 # 합치는 방법
#          on: 'IndexLabel | None' = None,       # 합치는 컬럼(컬럼명이 같을때)
#          left_on: 'IndexLabel | None' = None,  # 첫번째 데이터프레임에서 합칠 컬럼(컬럼명이 다를 때)
#          right_on: 'IndexLabel | None' = None) # 두번째 데이터프레임에서 합칠 컬럼(컬럼명이 다를 때)

pd.merge(emp, df_dept, on='deptno')
#    empno  ename  deptno   sal     dname
# 0      1  smith      10  4000    인사부
# 1      2  allen      10  4500    인사부
# 2      4  grace      10  4200    인사부
# 3      3   ford      20  4300    총부무
# 4      6   king      20  4000    총부무
# 5      5  scott      30  4100  IT분석팀

pd.merge(emp, df_dept, how='outer', on='deptno')
# 'outer' 옵션 때문에 둘 중 하나라도 값이 없으면 NaN
#   empno  ename  deptno   sal    dname
#0      1  smith      10  4000    인사부
#1      2  allen      10  4500    인사부
#2      4  grace      10  4200    인사부
#3      3   ford      20  4300    총부무
#4      6   king      20  4000    총부무
#5      5  scott      30  4100  IT분석팀

pd.merge(emp, df_dept, how='left', on='deptno')
# 'left' 옵션 때문에 emp 값 기준으로 병합
#    empno  ename  deptno   sal     dname
# 0      1  smith      10  4000    인사부
# 1      2  allen      10  4500    인사부
# 2      3   ford      20  4300    총부무
# 3      4  grace      10  4200    인사부
# 4      5  scott      30  4100  IT분석팀
# 5      6   king      20  4000    총부무

# 'outer' 옵션 좀 더 눈에 띄게 확인하는 예
df_dept_new = DataFrame({'deptno':[10,20], 'dname':['인사총무부','IT분석팀']})

pd.merge(emp, df_dept_new, on = 'deptno') 
# 30번 부서원 생략, 아무 옵션이 없으면 둘 중 하나라도 없으면 생략됨
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000  인사총무부
# 1      2  allen      10  4500  인사총무부
# 2      4  grace      10  4200  인사총무부
# 3      3   ford      20  4300  IT분석팀
# 4      6   king      20  4000  IT분석팀

pd.merge(emp, df_dept_new, how = 'outer', on = 'deptno')  
# 30번까지 포함(NaN으로 나옴), 둘 중 하나라도 있으면 나옴
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000  인사총무부
# 1      2  allen      10  4500  인사총무부
# 2      4  grace      10  4200  인사총무부
# 3      3   ford      20  4300  IT분석팀
# 4      6   king      20  4000  IT분석팀
# 5      5  scott      30  4100    NaN

pd.merge(emp, df_dept_new, how = 'left', on = 'deptno')
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000  인사총무부
# 1      2  allen      10  4500  인사총무부
# 2      3   ford      20  4300  IT분석팀
# 3      4  grace      10  4200  인사총무부
# 4      5  scott      30  4100    NaN
# 5      6   king      20  4000  IT분석팀
```