# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:03:03 2021

@author: sjh73
"""

# python pandas groupby
# 그룹연산
# 성별 성적 평균, 학년별 성적 최고점수, 부서별 평균 연봉 등
# groupby 메소드 처리 가능

import pandas as pd
from pandas import Series, DataFrame

f1 = pd.read_csv('./data/kimchi_test.csv', encoding='cp949')

f1.groupby?
# f1.groupby(
#     by=None,                 # 그룹핑 할 컬럼(기준)
#     axis: 'Axis' = 0,         # 그룹핑 연산 방향
#     level: 'Level | None' = None,  # 멀티 인덱스일 경우, 특정 레벨의 값을 그룹핑 컬럼으로 사용
#     as_index: 'bool' = True,
#     sort: 'bool' = True,
#     group_keys: 'bool' = True,
#     squeeze: 'bool | lib.NoDefault' = <no_default>,
#     observed: 'bool' = False,
#     dropna: 'bool' = True,                                     # 나머진 default 값 사용이 일반적
# )

# 예제) 제품별, 판매처 별(김치별)) 수량 총 합
f1.groupby(by=['제품']).sum()    # 제품별로 그룹화해서 합계
f1.groupby(by=['제품','판매처']).sum()    # 제품별, 판매처별로 그룹화해서 합계
f1.groupby(by=['제품','판매처'])['수량'].sum()   # 그 중에서 '수량' 열만 추출
f1.groupby(by=['제품','판매처']).sum()['수량']   # 그 중에서 '수량' 열만 추출

# 제품 기준, 수량과 판매금액 총 합
f1.groupby(by='제품').sum()[['수량','판매금액']]

# 멀티인덱스
f2 = f1.groupby(by=['제품','판매처'])['수량'].sum()

# 제품별, 판매처별(김치별) 수량 총합, 평균
f1.groupby(by=['제품','판매처'])['수량'].agg(['sum','mean'])

# agg : 여러 함수를 동시에 전달

# 예제) 제품별, 판매처별 수량 판매금액 총합, 평균
f1.groupby(by=['제품','판매처'])[['수량','판매금액']].agg(['sum','mean'])

# 예제) 제품별, 판매자별 수량은 총합, 판매금액은 평균만 > dict() 사용
f1.groupby(by=['제품','판매처'])[['수량','판매금액']].agg({'수량':'sum','판매금액':'mean'})

# 멀티 레벨을 갖는 경우의 groupby 연산
f2
type(f2)
f2.groupby(level=0).sum() # 제품별 총합
f2.groupby(level='제품').sum()
f2.groupby(by='제품').sum()   # by랑 level 차이가 뭐여..... 찾아볼 것
f2.groupby(level=1).sum() # 판매처별 총합









