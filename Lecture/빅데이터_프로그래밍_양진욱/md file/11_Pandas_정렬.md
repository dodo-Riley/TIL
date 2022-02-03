# 11. python_pandas_정렬

# 11.1. 현재 작업 폴더 확인

- `pwd` : `present working directory`의 약자. 현재 작업 중인 폴더의 경로를 보여준다.
    
    ```python
    pw
    # 'C:\\Users\\sjh73\\Desktop\\Code_SJH'
    ```
    

- `getcwd()` : `get current working directory`. `os 모듈`을 호출하고 입력하면, 현재 작업 중인 폴더의 경로를 보여준다.
    
    ```python
    import os
    os.getcwd()
    # 'C:\\Users\\sjh73\\Desktop\\Code_SJH'
    ```
    

# 11.2. sort 함수

- sort_index()
    - `Series`, `DataFrame` 호출 가능
    - `index`나 `column명`을 기준으로 정렬한다.

```python
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame

emp = pd.read_csv('./data/emp.csv')   # emp.csv 파일 읽어서 emp에 지정
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000

emp.ename      # emp의 ename 열 색인
emp['ename']   # emp의 ename 열 색인
# 0    smith
# 1    allen
# 2     ford
# 3    grace
# 4    scott
# 5     king
# Name: ename, dtype: object
# 결과를 Series로 반환

emp_idx = emp['empno']  # emp의 empno 열을 색인하고 emp_idx에 지정
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# 5    6
# Name: empno, dtype: int64

emp.iloc[:,1:]            # emp의 모든 행, 두 번째부터 마지막 열 색인
#    ename  deptno   sal
# 0  smith      10  4000
# 1  allen      10  4500
# 2   ford      20  4300
# 3  grace      10  4200
# 4  scott      30  4100
# 5   king      20  4000

emp.set_index('ename')  # ename 열을 새로운 index로 지정 
#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# scott      5      30  4100
# king       6      20  4000

emp = emp.set_index('ename')   # emp를 ename 열이 index가 되도록 새로 지정
emp.sort_index(ascending=True)  # index를 기준으로 오름차순 정렬, ascending=True 입력 안해도 동일한 결과
#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# king       6      20  4000
# scott      5      30  4100
# smith      1      10  4000

emp.sort_index(ascending=False)  # index를 기준으로 내림차순 정렬
#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# scott      5      30  4100
# king       6      20  4000
# grace      4      10  4200
# ford       3      20  4300
# allen      2      10  4500

emp.sort_index(axis=0)       # 행(index) 기준으로 정렬
#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# king       6      20  4000
# scott      5      30  4100
# smith      1      10  4000

emp.sort_index(axis=1)      # 열(column) 기준으로 정렬
#        deptno  empno   sal
# ename                     
# smith      10      1  4000
# allen      10      2  4500
# ford       20      3  4300
# grace      10      4  4200
# scott      30      5  4100
# king       20      6  4000
```

- sort_values()
    - `Series`, `DataFrame` 호출 가능
    - 본문의 값으로 정렬

```python
emp.sort_values(by='sal')    # sal 열의 값을 기준으로 오름차순으로 정렬
emp.sort_values('sal')       # sal 열의 값을 기준으로 오름차순으로 정렬
#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# king       6      20  4000
# scott      5      30  4100
# grace      4      10  4200
# ford       3      20  4300
# allen      2      10  4500

emp.sort_values(by='sal', ascending=False) # sal 열의 값을 기준으로 내림차순으로 정렬
#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# scott      5      30  4100
# smith      1      10  4000
# king       6      20  4000

emp.sort_values(by=['deptno','sal']) # [1순위, 2순위....]로 입력하면 그에 따라 정렬
#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# grace      4      10  4200
# allen      2      10  4500
# king       6      20  4000
# ford       3      20  4300
# scott      5      30  4100

emp.sort_values(by=['deptno','sal'], ascending=[True,False])  # deptno 기준일 때는 오름차순, sal 기준일 때는 내림차순으로 정렬
#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# grace      4      10  4200
# smith      1      10  4000
# ford       3      20  4300
# king       6      20  4000
# scott      5      30  4100
```