# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:18:39 2021

@author: sjh73
"""

# 판다스_문자열 메소드
# 기본 메소드 : 벡터 연산 불가능(매 원소마다 반복 불가)

'abc'.upper()
'a/b/c'.split('/')

l1 = ['abc','def']
l2 = ['a/b/c','d/e/f']
l1.upper()   # 불가
l2.upper()   # 불가

list(map(lambda x: x.upper(), l1))
list(map(lambda x: x.upper(), l2))
list(map(lambda x: x.split('/'), l2))

# 판다스 메소드 : 벡터 연산 가능(매 원소마다 반복 가능)
# Series, DataFrame 적용가능

from pandas import Series, DataFrame

# split
s1 = Series(l1)
s2 = Series(l2)

s2.split('/')  # 불가
s2.str.split('/')  # 가능

# 대소치환
s1.str.upper()
s1.str.lower()
s1.str.title()

# replace
s1.str.replace('a','A')
s1.str.replace('a','')

# 예제 
# 천단위 구분기호 처리 후 더하기
s3 = Series(['1,200','3,000','4,000'])
s3.str.replace(',','').astype(int).sum()

# 패턴확인 : starswith, endswith, contains

s1.str.startswith('a')
s1[s1.str.startswith('a')]  # 각 원소에서 'a'로 시작하는 원소 추출
s1[s1.str.endswith('c')]
s1[s1.str.contains('c')]

# 문자열 크기 len()
s1.str.len()

# count : 포함되어 있는 개수
Series(['avvva','dbfasv']).str.count('a')

# 문자열 제거(제거함수 : 공백, 문자)
Series(['    ab   ','     gf      ']).str.strip()
Series(['    ab   ','     gf      ']).str.strip().str.len()

s1.str.strip('a')
Series(['avadf','asdvasdf']).str.strip('a')  # 중간값제거불가
Series(['avadf','asdvasdf']).str.replace('a','') # 문자를 공백으로 대체 = 전부제거

# find : 위치값 리턴
s3 = Series(['sjh@naver.com','hjg@naver.com'])
s3.str.find('@')

# 문자열 색인(추출)
s3[0:1]  #시리즈에서 1번째 원소추출
s3.str[0:1]    #시리즈에서 각 원소마다 1번째 문자열 추출

# 예제) 이메일 아이디 추출
s3 = Series(['sjh@naver.com','hjg@naver.com'])
s4 = s3.str.find('@')
list(map(lambda x,y : x[0:y], s3,s4))  # @ 이전 문자 추출

list(s3.map(lambda x:x[:x.find('@')]))   # @ 이전 문자 추출

# pad : 문자열 삽입
# s1.str.pad(5,               # 총 자리수
#            'left',          # 삽입 방향
#            '!')             # 삽입 글자

s1
s1.str.pad(5,'left','!')
s1.str.pad(5,'right','*')

# 문자열 결합
'a'+'b'
'a'*3
s5 = Series(['abc','def','123'])
s5.str.cat()   # 시리즈 내 서로 다른 원소 결합
s5.str.cat(sep='/')

s6 = Series([['a','b','c'],['d','e','f']])
s6
s6.str.join(sep='')  # series 내 각 원소 내부의 문자열을 결합(구분기호가 공백)
s6.str.join(sep=',')  # series 내 각 원소 내부의 문자열을 결합(구분기호가 ,)


