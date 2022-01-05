# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:32:14 2021

@author: sjh73
"""

# 문자열 메소드
# 문자열 처리와 관련된 메소드

# 1. 기본 메소드 : 벡터 연산 불가(매 원소마다 반복 불가)

'abs'.upper()
'a/b/c'.split('/')
'a/b/c'.split('/')[1]

l1 = ['abd','def']
l2 = ['a/b/c','d/e/f']
l1.upper() # 불가
l2.split() # 불가

map(lambda x: x.upper(),l1)
list(map(lambda x: x.upper(),l1))

list(map(lambda x: x.split('/'),l2))
list(map(lambda x: x.split('/')[1],l2))


# pandas 메소드 : 백터화 내장(매 원소마다 반복 가능)
# series, dataframe

# 1) split
from pandas import Series, DataFrame
l1
Series(l1)

s1=Series(l1)

l2
Series(l2)
s2=Series(l2)

s2.str.split('/')

# 2) 대소 치환
s1.str.upper()
s1.str.lower()
s1.str.title()

# 3) replace  **중요**
s1.str.replace('a','A')
s1.str.replace('a','')

# 예제 - 천단위 구분기호 처리
s3 = Series(['1,200','3,000','4,000'])
s3.sum()
# 천 단위 구분기호 ',' 때문에 문자로 입력된 값이라 문자열 결합으로 인식한 결과 원하지 않는 값이 나옴

s3.str.replace(',','').astype('int').sum()  # ',' 공백으로 replace, 문자를 정수로 타입 변환, 합

# 4) 패턴 확인 : startswith, endswith, contains
s1.str.startswith('a')
s1[s1.str.startswith('a')] # s1 각 원소에서 'a'로 시작하는 원소 추출
s1[s1.str.endswith('c')]   # s1 각 원소에서 'c'로 끝나는 원소 추출
s1[s1.str.contains('e')]   # s1 각 원소에서 'e'가 들어가는 원소 추출

# 문자열 크기 len()
s1.str.len()
# 포함 개수 count()
Series(['asdfasdf','zcvzxcv']).str.count('a')
# 제거 함수(공백,문자)
Series(['as            ','          ab   ']).str.strip()
Series(['as            ','          ab   ']).str.strip().str.len()

s1
s1.str.strip('a') # 문자열 제거
Series(['aaavasdf','xvbdfgasdf']).str.strip('a')  # 중간에 값이 제거 안됨
Series(['aaavasdf','xvbdfgasdf']).str.replace('a','') # 중간에 값까지 사라짐

# find(위치값 return)
s3 = Series(['gvda@naver.com','asdv@naver.com'])
s3.str.find('@')

# 문자열 색인(추출)
'abcde'[0:3]  # 문자열 색인
s3[0:3]  # series에서 1,2,3 번째 원소 추출
s3.str[0:3] # series에서 각 원소마다 1,2,3번째 문자열 추출


s4 = Series(['sjh@naver.com','asdf@naver.com'])
s5 = s4.str.find('@')
s5
s4.str[0:]

list(map(lambda x,y : x[0:y], s4,s5))  # @ 이전 문자 추출

list(s4.map(lambda x:x[:x.find('@')]))   # @ 이전 문자 추출

# pad : 문자열 삽입
# s1.str.pad(5,               # 총 자리수
#            'left',          # 삽입 방향
#            '!')             # 삽입 글자

s1
s1.str.pad(5,'left','!')

# 문자열 결합
'a'+'b'
'a'*3
s5 = Series(['abc','def','123'])
s5.str.cat()
s5.str.cat(sep='/')
s6 = Series([['a','b','c'],['d','e','f']])
s6

s6.str.join(sep='')  # series 내 각 원소 내부의 문자열을 결합(구분기호가 공백)
s6.str.join(sep=',')  # series 내 각 원소 내부의 문자열을 결합(구분기호가 ,)
