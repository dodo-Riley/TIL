# 20. Pandas_연습문제(2)

# 20.1. 문제 1 : card.csv

- 일자별 총 지출 금액을 구하고, 이를 마지막 열로 추가하기
    
    ```python
    import pandas as pd
    import numpy as np
    from pandas import Series, DataFrame
    
    card = pd.read_csv('./data/card.csv', encoding='cp949')
    card = card.set_index('NUM') # NUM 열을 인덱스로 사용
    
    card_int = card.applymap(lambda x: int(x.replace(',','')))
    card_int['총 지출 금액'] = card_int.sum(axis=1)
    card_int
    ```
    

- 식료품 컬럼만 천단위 제거하고 숫자로 변경
    
    ```python
    card_food_int = card
    card_food_int['식료품'] = card['식료품'].apply(lambda x: int(x.replace(',','')))
    # apply 대신 map도 가능
    # card['식료품'].str.replace(',','').astype('int')도 가능
    card_food_int
    ```
    

- 책값 컬럼만 천단위 제거하고 숫자로 변경
    
    ```python
    card_book_int = card
    card_book_int['책값'] = card['책값'].str.replace(',','').astype('int')
    card_book_int
    ```
    

- 일자별로 각 품목별 지출 비용을 퍼센트로 출력
    
    ```python
    # 반복문 사용
    for i in range(len(card_int)) :
    	(card_int.iloc[i,:-1] / card_int.iloc[i,:-1].sum())*100
    
    # apply 메소드 이용, 각 일자별로 적용
    card_int2 = card.applymap(lambda x: int(x.replace(',','')))
    card_int2.apply(lambda x: (x/x.sum())*100, axis=1)
    ```
    

# 20.2. 문제 2 : ex_test1.csv

- 각 구매마다 포인트 확인하고, point 컬럼 생성(단, point는 주문금액 5만원 미만 1%, 5만이상 10만 미만 2%, 10만이상 3%)
    
    ```python
    import pandas as pd
    import numpy as np
    from pandas import Series, DataFrame
    
    df = pd.read_csv('./data/ex_test1.csv', encoding = 'cp949')
    
    if df['주문금액'] < 50000 :
    	df['주문금액']*0.01
    # if 문은 여러개의 bool 연산 불가
    
    # Solution_1) for, if 사용
    result = []
    
    for i in df['주문금액'] :
    	if i < 50000 :
    		result.append(i*0.01)
    	elif i < 100000 :
    		result.append(i*0.02)
    	else :
    		result.append(i*0.03)
    
    df['POINT'] = np.round(result,2)  # 결과가 실수형으로 길게 나오므로 소수점 2자리까지만 반올림으로
    
    # Solution_2) np.where 사용
    # np.where(조건, 참 리턴, 거짓 리턴) : sql의 select * from db_name where 조건절 형태를 따옴
    df['POINT_2'] = np.where(df['주문금액']<50000,df['주문금액']*0.01,
    np.where(df['주문금액']<100000,df['주문금액']*0.02,df['주문금액']*0.03))
    ```
    

- 회원번호별 총 주문금액과 총 포인트 금액 확인
    
    ```python
    df.groupby('회원번호')[['주문금액','POINT']].sum()
    ```
    

# 20.3. 문제 3 : 요소 변경

- Y 값을 서로 다른 숫자로 변경
    
    ```python
    df2 = DataFrame({'Y' : ['a','a','b','b','c','a','a','b'],
                     'X1' : [1,2,4,4,6,3,5,4],
                     'X2' : [10,30,43,34,43,43,94,32]})
    
    # 하나씩 사용자가 치환
    df2['Y'].replace({'a':0, 'b':1, 'c':2})
    
    # 자동 변환 함수 사용
    from sklearn.preprocessing import LabelEncoder
    
    m_lb = LabelEncoder()
    m_lb.fit_transform(df2['Y'])
    ```
    
- df2에서 X1이 5 이상일 경우, X1 평균(또는 최빈값, 중앙값, 최소값)으로 수정
    
    ```python
    df2['X1'][df2['X1']>=5] # df2의 X1 열에서 5이상인 값 색인
    df2.loc[df2['X1']>=5, 'X1'] # df2의 X1 열에서 5이상인 값 색인
    
    m1 = df2['X1'].mean() # 평균
    m2 = df2['X1'].median() # 중앙값
    m3 = df2['X1'].mode() # 최빈값(데이터 타입이 Series) 
    m4 = df2['X1'].mode()[0] # 최빈값 데이터 타입을 정수로 바꾸기
    
    # import statistics as stat
    # stat.mode(df2['X1'])       # 바로 정수형으로 최빈값 추출
    
    m5 = df2['X1'].min() # 최소값
    m6 = df2['X1'].max() # 최대값
    
    df2.loc[df2['X1']>=5, 'X1'] = m3 # m3의 데이터 타입이 Series이므로 불가
    df2.loc[df2['X1']>=5, 'X1'] = m4 # m4는 정수형이므로 가능
    ```