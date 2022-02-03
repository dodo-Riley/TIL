# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 13:14:19 2021

@author: sjh73
"""

# 14. drop, shift, rename

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

run my_modules # 매번 import하기 귀찮으니까 미리 파일 생성해두고 실행

# 1. drop
# 특정 행, 컬럼 제거
# 이름 전달

emp = pd.read_csv("./data/emp.csv")
emp
emp['ename'] == 'scott' # 'ename' 컬럼 중 'scott'인지 아닌지
emp.loc[emp['ename'] == 'scott'] # 'ename' 컬럼 중 'scott'인 행
emp.loc[emp['ename'] == 'scott',:] # 'ename' 컬럼 중 'scott'인 행, 모든 열
emp.loc[~(emp['ename'] == 'scott'),:] # 'ename' 컬럼 중 'scott'이 아닌 행, 모든 열
emp.drop(4, axis=0) # 행기준, 4번째 idx 제외

# 예제) emp 데이터셋에서 sal 컬럼 제외
emp.iloc[:,0:3]
emp.iloc[:,:-1]
emp.drop('sal', axis=1)
emp.loc[:,'empno':'deptno']


emp.drop(['ename','deptno'], axis=1)

# 2. shift
# 행 또는 열을 이동
# ex) 전일 대비 증감율 구할 때

emp
emp['sal'].shift() # default : 1행, axis=0 기준

# 예제) 다음 데이터 프레임에서 전일 대비 증감율 출력
s1 = Series([3000,3500,4200,2800,3600], index=['2021/01/01','2021/01/02','2021/01/03','2021/01/03','2021/01/05'])
s1
s2 = s1.shift()
((s1-s2)/s1)*100

# 3. rename
# 행, 컬럼명 변경

emp
emp.columns = ['emptno','ename','deptno','salary']
emp.rename({'salary':'sal','deptno':'dept_no'}, axis=1)
emp.rename({0:'a',2:'b'}, axis=0)

# 예제) emp 데이터에서 ename을 index로 설정 scott을 대문자로 변경
emp
emp_re = emp.set_index('ename')
emp_up = emp_re.rename({'scott':'SCOTT'}, axis=0)

emp.set_index('ename').rename({'scott':'SCOTT'})

