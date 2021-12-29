# 08. Pandas_문자열 메소드

> 기본 메소드는 벡터 연산이 불가능하지만, 판다스에서는 `.str`을 통해  벡터 연산이 가능하다(매 원소마다 반복 가능)
> 

- split
    
    ```python
    from pandas import Series, DataFrame
    
    l1 = ['abc','def']
    l2 = ['a/b/c','d/e/f']
    
    s1 = Series(l1) 
    s2 = Series(l2)
    
    s2.split('/') # 불가 
    s2.str.split('/') # 가능
    ```
    

- 대소치환
    
    ```python
    s1.str.upper() 
    s1.str.lower() 
    s1.str.title()
    ```
    

- replace
    
    ```python
    s1.str.replace('a','A') 
    s1.str.replace('a','')
    
    # 천단위 구분기호 처리 후 더하기
    
    s3 = Series(['1,200','3,000','4,000']) 
    s3.str.replace(',','').astype(int).sum()
    ```
    

- starswith, endswith, contains
    
    ```python
    s1.str.startswith('a') 
    s1[s1.str.startswith('a')] # 각 원소에서 'a'로 시작하는 원소 추출 
    s1[s1.str.endswith('c')] 
    s1[s1.str.contains('c')]
    ```
    

- len()
    
    ```python
    s1.str.len()
    # 0    3
    # 1    3
    # dtype: int64
    ```
    

- count
    
    ```python
    Series(['avvva','dbfasv']).str.count('a')
    # 0    2
    # 1    1
    # dtype: int64
    ```
    

- 문자열 제거
    
    ```python
    Series([' ab ',' gf ']).str.strip() 
    Series([' ab ',' gf ']).str.strip().str.len()
    s1.str.strip('a') 
    Series(['avadf','asdvasdf']).str.strip('a') # 중간값 제거불가 
    Series(['avadf','asdvasdf']).str.replace('a','') # 문자를 공백으로 대체 = 전부제거
    ```
    

- find : 위치값 리턴
    
    ```python
    s3 = Series(['sjh@naver.com','hjg@naver.com']) 
    s3.str.find('@')
    # 0    3
    # 1    3
    # dtype: int64
    ```
    

- 문자열 색인(추출)
    
    ```python
    s3[0:1] # 시리즈에서 1번째 원소추출 
    s3.str[0:1] # 시리즈에서 각 원소마다 1번째 문자열 추출
    
    # 이메일 아이디 추출
    s3 = Series(['sjh@naver.com','hjg@naver.com']) 
    s4 = s3.str.find('@') 
    
    list(map(lambda x,y : x[0:y], s3,s4)) # @ 이전 문자 추출
    list(s3.map(lambda x:x[:x.find('@')])) # @ 이전 문자 추출
    ```
    

- pad : 문자열 삽입
    
    ```python
    s1.str.pad(5, # 총 자리수
    #     'left', # 삽입 방향
    #        '!') # 삽입 글자
    
    s1.str.pad(5,'left','!') 
    # 0    !!abc
    # 1    !!def
    # dtype: object
    s1.str.pad(5,'right','*')
    ```
    

- cat : 문자열 결합
    
    ```python
    s5 = Series(['abc','def','123']) 
    s5.str.cat()
    # abcdef123
    # 시리즈 내 서로 다른 원소 결합
     
    s5.str.cat(sep='/')
    # abc/def/123
    # 시리즈 내 서로 다른 원소 결합, '/'로 구분
    
    s6 = Series([['a','b','c'],['d','e','f']]) 
    s6.str.join(sep='') 
    # 0    abc
    # 1    def
    # dtype: object
    # series 내 각 원소 내부의 문자열을 결합(구분기호 없음) 
    
    s6.str.join(sep=',') 
    # series 내 각 원소 내부의 문자열을 결합(구분기호가 ',')
    ```