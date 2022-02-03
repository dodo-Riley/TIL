# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:13:24 2022

@author: sjh73
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import random

# card.csv 파일 읽기

card = pd.read_csv('./data/card.csv', encoding='cp949')
card

# NUM 열을 인덱스로

card = card.set_index('NUM')

# 일자별 총 지출 금액을 구해서, 마지막 걸럼에 추가(천 단위 구분 기호 제거 후 숫자로 변경)

card_int = card.applymap(lambda x: int(x.replace(',','')))
card_int['총 지출 금액'] = card_int.sum(axis=1)
card_int

# 식료품 컬럼만 천단위 제거하고 숫자로 변경
card_food_int = card
card_food_int['식료품'] = card['식료품'].apply(lambda x: int(x.replace(',',''))) 
# apply 대신 map도 가능
# card['식료품'].str.replace(',','').astype('int)도 가능
card_food_int

# 책값 컬럼만 천단위 제거하고 숫자로 변경
card_book_int = card
card_book_int['책값'] = card['책값'].str.replace(',','').astype('int')
card_book_int

# 일자별로 각 품목별 지출 비용을 퍼센트로 출력

card_int_rate = card_int.div(card_int['총 지출 금액'], axis=0)

(card_int.iloc[0,:-1] / card_int.iloc[0,:-1].sum())*100
# 모든 행에대해서 반복돌려야됨

# apply 메소드 이용, 각 일자별로 적용
card_int2 = card.applymap(lambda x: int(x.replace(',','')))

card_int2.apply(lambda x: (x/x.sum())*100, axis=1)

# 결과 해석
# 의복비 지출이 심함(일자별 지출 중 의복비 비중이 50%이상)
# insight : 의복비 비용을 줄여야함(주관적 의견)

# 형 변환 : 함수, astype 메소드
# 적용함수 : map, apply, applymap
# 치환함수 : replace, str.replace
# 색인
# 컬럼 추가 및 내용 변경





# 각 구매마다 포인트 확인하고, point 컬럼 생성
# point는 주문금액 5만원 미만 1%, 5만이상 10만 미만 2%, 10만이상 3$

df = pd.read_csv('./data/ex_test1.csv', encoding = 'cp949')

if df['주문금액'] < 50000 :
    df['주문금액']*0.01
# if 문은 여러개의 bool 연산 불가

# 답1) for, if 사용
result = []

for i in df['주문금액'] :
    if i < 50000 :
        result.append(i*0.01)
    elif i < 100000 :
        result.append(i*0.02)
    else :
        result.append(i*0.03)

df['POINT'] = np.round(result,2)


# 답2) np.where 사용
# sql의 select * from db_name where 조건절 형태를 따옴
# np.where(조건, 참 리턴, 거짓 리턴)

df['POINT_2'] = np.where(df['주문금액']<50000,df['주문금액']*0.01,
         np.where(df['주문금액']<100000,df['주문금액']*0.02,df['주문금액']*0.03))


# 회원번호별 총 주문금액과 총 포인트 금액 확인
df.groupby('회원번호')[['주문금액','POINT']].sum()




# Y 값을 서로 다른 숫자로 변경
df2 = DataFrame({'Y' : ['a','a','b','b','c','a','a','b'],
           'X1' : [1,2,4,4,6,3,5,4],
           'X2' : [10,30,43,34,43,43,94,32]})
# 하나씩 사용자가 치환
df2['Y'].replace({'a':0, 'b':1, 'c':2})

# 자동 변환 함수
from sklearn.preprocessing import LabelEncoder

m_lb = LabelEncoder()
m_lb.fit_transform(df2['Y'])

# 조건에 따른 값의 수정
# df2에서 X1이 5 이상일 경우, X1 평균으로 수정(최빈값, 중앙값, 최소값)

df2['X1'][df2['X1']>=5]

df2.loc[df2['X1']>=5, 'X1']

df2
m1 = df2['X1'].mean()
m2 = df2['X1'].median()
m3 = df2['X1'].mode() # 최빈값 구하기
m4 = df2['X1'].mode()[0]
# import statistics as stat
# stat.mode(df2['X1'])
m5 = df2['X1'].min()
m6 = df2['X1'].max()




df2.loc[df2['X1']>=5, 'X1'] = m3 # 안됨
df2.loc[df2['X1']>=5, 'X1'] = m4 # 됨
