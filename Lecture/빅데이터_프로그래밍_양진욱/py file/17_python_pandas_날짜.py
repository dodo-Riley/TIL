# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:22:34 2021

@author: sjh73
"""

# 날짜 표현
# 월별, 일별, 요일별 집계
# 현재 날짜 - 입사일자 = 근무일자

# 현재 날짜
run my_modules

from datetime import datetime

datetime.now() # 현재 년월일,시분초
d1 = datetime.now()
type(d1)

d1.year
d1.month
d1.day

# 날짜 파싱
d2 = '2022/01/01'
d2.year # error

datetime.strptime(date_string, format)
datetime.strptime(d2, '%Y/%m/%d')
datetime.strptime('09/12/25', '%m/%d/%y')

# 벡터 연산이 안됨
# Series는 벡터 연산이 불가
s1 = Series(['2022/01/01', '2022/01/02', '2022/01/03'])
datetime.strptime(s1, '%Y/%m/%d')
# 해결 : map
s1.map(lambda x: datetime.strptime(x,'%Y/%m/%d'))

# 해결 : pd.to_datetime(벡터 연산 가능)
pd.to_datetime(s1)
s2 = pd.to_datetime(s1)
# pd.to_datetime(s2, format = '%Y/%m/%d') 왜 안됨?

# 날짜 포맷 변경 
# datetime.strftime(string format time)
# 요일 추출(날짜에서 요일을 return하도록 날짜 출력 형식 변경)
# ex) (년/월/일) > (월/일/년) 순서로 변경
# 날짜 포맷 변경 한 후 반환된 값은 문자열이다
d1 = datetime.now()
d1
datetime.strftime(d1, '%A') # 요일 리턴
datetime.strftime(d1, '%m-%d, %Y') # '12-29, 2021'
datetime.strftime(d1, '%m-%d, %y') # '12-29, 21'
datetime.strftime(d1, '%Y')

s2
datetime.strftime(s2, '%Y') # Series는 불가
s2.map(lambda x: datetime.strftime(x,'%Y')) # map을 이용해서 적용

# 날짜 연산
d1 = datetime.now()  # 현재 시간
# offset
from pandas.tseries.offsets import Day, Hour, Second
d1 + Day(100)   # d1으로부터 100일 뒤
# timedelta
from datetime import timedelta
d1 + timedelta(100)   # d1으로부터 100일 뒤
# DateOffset
d1 + pd.DateOffset(months = 4)  # 4달 뒤
# 날짜 - 날짜
d2 = '2022/01/01'
d1 - datetime.strptime(d2, '%Y/%m/%d')
d3 = d1 - datetime.strptime(d2, '%Y/%m/%d')
d3.days
d3.seconds

# 예제) 요일별 통화건수 총합
deli = pd.read_csv('./data/delivery.csv', encoding = 'cp949')
deli.dtypes
deli.head()
deli.info()
deli.describe()

deli['일자'] = pd.to_datetime(deli['일자'], format = '%Y%m%d')
deli

datetime.strftime(deli['일자'], '%A') # 불가능
deli['요일'] = deli['일자'].map(lambda x: datetime.strftime(x,'%A')) # map 활용
deli.groupby('요일')['통화건수'].sum()

total = deli.groupby('요일')['통화건수'].sum()
total[['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']] # sort 적용 불가능함
