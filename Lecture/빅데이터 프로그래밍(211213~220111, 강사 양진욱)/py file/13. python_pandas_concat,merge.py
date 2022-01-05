# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:21:08 2021

@author: sjh73
"""

# merge
# 행이 서로 분리되어 있는 하나의 데이터프레임으로 합치기
# 컬럼이 서로 분리되어 있는 하나의 데이터프레임으로 합치기
# 참조 조건 사용, 연관된 두 데이터를 병합(join)

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# concat

df1 = DataFrame(np.arange(1,7).reshape(2,3), columns=['A','B','C'])
df2 = DataFrame(np.arange(10,61,10).reshape(2,3), columns=['A','B','C'])

pd.concat([df1,df2])  # 행의 결합 > 기본은 세로 방향으로 합쳐짐
pd.concat([df1,df2],axis=0)   # 행의 결합 > 세로 방향으로 합쳐짐
pd.concat([df1,df2],axis=1)   # 열의 결합 > 가로 방향으로 합쳐짐
pd.concat([df1,df2], ignore_index=True)  # 합칠 때, 기존 인덱스 무시하고 순차적으로 번호 부여

# join
# 두 데이터 프레임(테이블) 참조조건 활용, 하나의 객체로 합치거나 데이터 처리
# merge가 두 데이터프레임 조인을 수행, 등가 조건만을 사용하여 조인이 가능

emp = pd.read_csv('./data/emp.csv')
df_dept = DataFrame({'deptno':[10,20,30],'dname':['인사부','총부무','IT분석팀']})

# pd.merge(
#     left: 'DataFrame | Series',   # 왼쪽에 붙을 자료
#     right: 'DataFrame | Series',  # 오른쪽에 붙을 자료
#     how: 'str' = 'inner',         # 합치는 방법
#     on: 'IndexLabel | None' = None,   # 합치는 컬럼(컬럼명이 같을때)
#     left_on: 'IndexLabel | None' = None,   # 첫번째 데이터프레임에서 합칠 컬럼(컬럼명이 다를 때)
#     right_on: 'IndexLabel | None' = None,  # 두번째 데이터프레임에서 합칠 컬럼(컬럼명이 다를 때)
#     left_index: 'bool' = False,
#     right_index: 'bool' = False,
#     sort: 'bool' = False,
#     suffixes: 'Suffixes' = ('_x', '_y'),
#     copy: 'bool' = True,
#     indicator: 'bool' = False,
#     validate: 'str | None' = None,
# ) -> 'DataFrame'


pd.merge(emp, df_dept, on='deptno')
pd.merge(emp, df_dept, how='outer', on='deptno')
pd.merge(emp, df_dept, how='left', on='deptno')

# outer join
df_dept_new = DataFrame({'deptno':[10,20], 'dname':['인사총무부','IT분석팀']})
pd.merge(emp, df_dept_new, on = 'deptno') # 30번 부서원 생략
pd.merge(emp, df_dept_new, how = 'outer', on = 'deptno')  # 30번까지 포함(NaN으로 나옴)
pd.merge(emp, df_dept_new, how = 'left', on = 'deptno')
