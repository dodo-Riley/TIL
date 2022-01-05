# 17. Pandas_날짜

# 17.1. 현재 날짜

```python
run my_modules
from datetime import datetime

datetime.now() 
# 현재 년월일,시분초
# datetime.datetime(2022, 1, 1, 13, 34, 25, 909487)

d1 = datetime.now()
type(d1)
# datetime.datetime

d1.year   # 2022
d1.month  # 1
d1.day    # 1
```

# 17.2. 날짜 포맷 코드

- 날짜를 나타내는 포맷 코드는 아래와 같다.
    
    
    | 포맷 코드 | 설명 | 예 |
    | --- | --- | --- |
    | %a | 요일을 짧게 표시합니다. | Sun |
    | %A | 요일을 길게 표시합니다. | Sunday |
    | %w | 요일을 숫자로 표시합니다. 일요일을 0부터 시작하여 토요일은 6입니다. | 0 |
    | %d | 날(day)을 출력합니다. 1부터 31까지가 있겠죠 | 18 |
    | %b | 월을 영어로 짧게 출력해줍니다. | Apr |
    | %B | 월을 영어로 길게 출력해줍니다. | April |
    | %m | 월을 숫자로 표현합니다. | 04 |
    | %y | 년을 짧게 숫자로 표시합니다 | 21 |
    | %Y | 년을 길게 숫자로 표시합니다. | 2021 |
    | %H | 시간을 24시간의 표현 방식(00-23)으로 숫자로 표시합니다. | 18 |
    | %I | 시간을 0-12시 표시 방법으로 표시합니다 | 6 |
    | %p | 오전(AM), 오후(PM)을 표시합니다. | PM |
    | %M | 분(0 - 59)을 표시합니다. | 38 |
    | %S | 초(0 - 59)를 표시합니다. | 55 |
    | %f | microsecond단위를 표시합니다. | 545433 |
    | %j | 일년중 몇번째일인지 나타냅니다. | 108 |
    | %U | 일년 중 몇번째 주 인지 나타내니다. 이 포맷에서 일요일은 일주일의 시작입니다. 일년은 52주, 53주입니다. | 108 |
    | %W | 일년 중 몇번째 주 인지 나타내는 것은 %U와 같지만 일주일의 시작을 월요일로 정합니다. | 108 |
    | %c | Local version의 날짜와 시간을 나타냅니다. | Sun Apr 18 17:26:26 2021 |
    | %x | Local version의 날짜만 나타냅니다. | 04/18/21 |
    | %X | Local version의 시간만 나타냅니다. | 17:26:26 |

> 출처 및 참고 : [https://reakwon.tistory.com/172](https://reakwon.tistory.com/172)
> 

# 17.3. strptime과 strftime

- strptime
    - 문자열을 `datetime type`으로 변환한다.
        
        ```python
        d2 = '2022/01/01'
        d2.year # d2가 datetime이 아니라 문자열이기 때문에 error
        
        # datetime.strptime(date_string, format)
        
        datetime.strptime(d2, '%Y/%m/%d')
        # datetime.datetime(2022, 1, 1, 0, 0)
        
        datetime.strptime('09/12/25', '%m/%d/%y')
        # datetime.datetime(2025, 9, 12, 0, 0)
        
        s1 = Series(['2022/01/01', '2022/01/02', '2022/01/03'])
        datetime.strptime(s1, '%Y/%m/%d')
        # Series는 벡터 연산이 불가하므로 error
        # map()이나 판다스의 to_datetime()을 사용하면 Series도 가능
        
        s1.map(lambda x: datetime.strptime(x,'%Y/%m/%d'))
        # 0   2022-01-01
        # 1   2022-01-02
        # 2   2022-01-03
        # dtype: datetime64[ns]
        
        pd.to_datetime(s1)
        # 0   2022-01-01
        # 1   2022-01-02
        # 2   2022-01-03
        # dtype: datetime64[ns]
        ```
        

- strftime
    - `datetime type`을 문자열로 변환한다.
        
        ```python
        d1 = datetime.now()
        datetime.strftime(d1, '%A') # 'Saturday', 요일 리턴
        datetime.strftime(d1, '%m-%d, %Y') # '01-01, 2022'
        datetime.strftime(d1, '%m-%d, %y') # '01-01, 22'
        datetime.strftime(d1, '%Y')  # '2022'
        
        s2 = pd.to_datetime(s1) # Series의 문자열 요소들을 datetime으로 변경
        datetime.strftime(s2, '%Y') # Series는 벡터 연산이 불가
        
        s2.map(lambda x: datetime.strftime(x,'%Y')) 
        # map을 이용해서 적용
        # 0    2022
        # 1    2022
        # 2    2022
        # dtype: object
        ```
        

# 17.4. 날짜 연산

- offset
    
    ```python
    d1 = datetime.now()  # 현재 시간
    
    from pandas.tseries.offsets import Day, Hour, Second
    
    d1 + Day(100)   # d1으로부터 100일 뒤
    ```
    

- timedelta
    
    ```python
    from datetime import timedelta
    
    d1 + timedelta(100)   # d1으로부터 100일 뒤
    ```
    

- DateOffset
    
    ```python
    d1 + pd.DateOffset(months = 4)  # 4달 뒤
    ```
    

- 날짜 - 날짜
    
    ```python
    d2 = '2022/01/20'
    
    d3 = d1 - datetime.strptime(d2, '%Y/%m/%d')
    # datetime type끼리 연산이 가능
    
    d3.days
    d3.seconds
    ```
    

# 17.5. 예제

```python
# 요일별 통화건수 총 합 구하기

deli = pd.read_csv('./data/delivery.csv', encoding = 'cp949')

deli.dtypes
# 자료형 확인
# 일자       int64
# 시간대      int64
# 업종      object
# 시도      object
# 시군구     object
# 읍면동     object
# 통화건수     int64
# dtype: object

deli.head()
deli.info()
deli.describe()   # 대략적인 자료에 대한 정보 확인

deli['일자'] = pd.to_datetime(deli['일자'], format = '%Y%m%d')
# '일자'열의 자료들을 datetime type으로 변경

datetime.strftime(deli['일자'], '%A') # Series라 불가능
deli['요일'] = deli['일자'].map(lambda x: datetime.strftime(x,'%A')) 
# map 활용, 일자에서 요일로 변환해 '요일' 컬럼 추가

total = deli.groupby('요일')['통화건수'].sum()
# '요일' 컬럼 기준으로 그룹화, 통화 건수의 총합을 total에 지정
# 요일
# Friday       162037
# Monday       142157
# Saturday     196429
# Sunday       196096
# Thursday     150316
# Tuesday      158544
# Wednesday    176357
# Name: 통화건수, dtype: int64

total[['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']] 
# sort 적용 불가능하므로 직접 요일 순으로 변경
```