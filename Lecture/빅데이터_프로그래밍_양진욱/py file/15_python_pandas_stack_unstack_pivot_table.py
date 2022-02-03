# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:25:55 2021

@author: sjh73
"""

# stack, unstack, pivot_table


# 자료구조(data type) 형태
# long data(tidy data) : 각 속성을 컬럼으로 표현
# wide data(cross table, 교차표) : 하나의 속성을 갖는 데이터가 각 종류마다 서로 다른 컬럼으로 분리되어 나열

# 1. stack / unstack
# stack : wide data > long data
# unstack : long data > wide data

import numpy as np    
import pandas as pd
from pandas import Series, DataFrame

kimchi = pd.read_csv('./data/kimchi_test.csv', encoding='cp949')
# kimchi 데이터를 연도별, 제품별 수량의 총합
df1 = kimchi.groupby(['판매년도','제품'])['수량'].sum()

# 멀티 인덱스
# 인덱스나 컬럼이 여러 레벨로 표현
# 상위레벨 : 0, 하위레벨로 갈 수록 숫자 증가

df2 = df1.unstack()
df3 = df2.stack()

df1.unstack(level=0) # 상위 레벨(연도)을 기준으로, default
df1.unstack(level=1) # 하위 레벨(제품)을 기준으로

# 2. pivot table
# 교차표 작성

kimchi.pivot_table(index = '판매월',       # index 방향에 배치할 컬럼명
                   columns = '판매처',     # column 방향에 배치할 컬럼명
                   values = '수량',        # 교차표에 작성할 값을 갖는 컬럼
                   aggfunc = 'sum')        # 그룹 함수

# 예제) kimchi 데이터를 이용해, 연도별/제품별 판매금액의 총 합을 교차표로 작성
kimchi.pivot_table(index = '판매년도', columns = '제품', values = '판매금액', aggfunc = 'sum')
