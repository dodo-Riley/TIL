# 10. Pandas_replace

# 1. 기본 문자열 메소드

- `Python`에서 기본 제공
- 문자열에서 호출 가능(리스트와 같은 자료형에서 불가)
- 벡터 연산(각 원소별 반복 처리) 불가능
- 오직 문자열 치환만 가능(숫자 치환, NA 치환 불가능)

```python
'abcd'.replace('a','A') # 'Abcd' >> a를 A로 치환 
'abcd'.replace('a','') # 'bcd' >> a를 공백으로 치환 

'abcd1'.replace(1,'') # TypeError: replace() argument 1 must be str, not int
' bcd1'.replace('',1) # 숫자로 치환하는거 안됨

['abcd','abcde','aabb'].replace(',','') # AttributeError: 'list' object has no attribute 'replace'

# 리스트 자료형일 경우, for문 활용

l1 = [] 
for i in ['abcd','abcde','aabb']: 
	l1.append(i.replace('a','A')) 
print(l1) 
# ['Abcd', 'Abcde', 'AAbb']

# 리스트 자료형일 경우, map 함수 활용

l1 = ['abcd','abcde','aabb']
f1 = lambda x: x.replace('a','A') 
list(map(f1, l1)) 
# ['Abcd', 'Abcde', 'AAbb']

# 참고

l1.map(f1) 
# AttributeError: 'list' object has no attribute 'map' 
# 리스트 객체는 map함수 호출 불가

from pandas import Series, DataFrame 

Series(l1).map(f1)  
# 시리즈는 호출 가능(method chaining)

import numpy as np 

Series(['abcd','abcde','aabb',np.nan]).map(lambda x: x.replace(np.nan,'')) 
# TypeError: replace() argument 1 must be str, not float 
# NaN이 문자열이 아니라 에러
```

# 2. .str.replace

- `pandas` 제공(`Series` 객체만 호출 가능)
- 벡터화 내장된 문자열 메소드
- 문자열 호출 가능
- 벡터연산(각 원소별 반복처리) 가능
- 오직 문자열 치환만 가능(숫자나 NA 치환 불가능)
- 숫자로 구성된 `Series` 적용 불가능

```python
Series(['abcd','abcde','aabb']).str.replace('a','A') 
# 0 Abcd 
# 1 Abcde 
# 2 AAbb 
# dtype: object

['abcd','abcde','aabb'].str.replace('a','A') 
# AttributeError: 'list' object has no attribute 'str' 
# list는 호출 불가능

DataFrame(['abcd','abcde','aabb']).str.replace('a','A') 
# AttributeError: 'DataFrame' object has no attribute 'str' 
# 데이터 프레임도 불가능
```

# 3. pandas replace

- `pandas` 제공
- 값 치환 메소드(똑같은, 완전히 일치하는 값을 다른 값으로 대체, 삭제)
- `Series`, `DataFrame` 호출 가능
- 숫자, NaN 치환 가능
- 동시에 여러 대상 수정 가능

```python
df1 = DataFrame([['1,200','1,300'],['1,400','1,500']]) 
df1 
#       0     1 
# 0 1,200 1,300 
# 1 1,400 1,500

df1.replace(',','') 
#       0     1 
# 0 1,200 1,300 
# 1 1,400 1,500 
# ','와 완전히 일치하는 값이 없기 때문에 변경점이 없다.

df2 = DataFrame([['1,200',','],['1,400','1,500']]) 
df2.replace(',','') 
#       0     1 
# 0 1,200
# 1 1,400 1,500 
# 완전히 똑같은 경우, 치환됨

df3 = DataFrame([['1200','1300'],['1400','.']], columns = ['a','b']) 
df3 
#      a    b 
# 0 1200 1300 
# 1 1400    .

df3.replace('.', np.nan) 
#      a    b 
# 0 1200 1300 
# 1 1400  NaN 
# '.'와 완전히 일치하는 값은 NaN 치환

df3.replace(['.', '1400', '?', '/'], np.nan) 
#      a    b 
# 0 1200 1300 
# 1  NaN  NaN 
# 만약 ’1400’이 아니라 1400치면 안바뀜
# 이유는 데이터프레임 안에 숫자가 아니라 스트링이기 때문
```

# 4. 연습문제

- `df1`의 천 단위 구분기호 제거 후 숫자로 변경하기
- `df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])`

```python
df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])
for i in range(len(df1)): 
	df1[i] = df1[i].str.replace(',', '').astype('int') 
print(df1)
# for문을 사용해 데이터프레임의 각 인덱스 별로 반복 수행

df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])
for i in range(len(df1)): 
	if df1[i].all() != 'int':
		df1[i] = df1[i].str.replace(',', '').astype('int') 
	else: 
		pass 
print(df1)
# 만약 주어진 df1의 각 인덱스별로 구성요소가 정수가 아니면, ','제거 후 정수로 변경
# 정수라면 pass

# applymap 활용 답
# applymap()은 데이터프레임에 사용, map()은 시리즈에 사용
# 요소별로 함수를 적용함

df1.applymap(lambda x: int(x.replace(',',''))) 
# scala에서는 문자열이 아닌 숫자로 변경해야함
 
df1.applymap(lambda x: int(x.replace(',',''))).sum()
```