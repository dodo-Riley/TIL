# 15. Pandas_stack, unstack, pivot_table

# 15.1. 자료구조(data type) 형태

- long data(tidy data) : 각 속성을 컬럼으로 표현
- wide data(cross table, 교차표) : 하나의 속성을 갖는 데이터가 각 종류마다 서로 다른 컬럼으로 분리되어 나열

# 15.2. stack / unstack

- stack : wide data > long data
- unstack : long data > wide data

```python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

kimchi = pd.read_csv('./data/kimchi_test.csv', encoding='cp949')

df1 = kimchi.groupby(['판매년도','제품'])['수량'].sum()
# kimchi 데이터를 연도별, 제품별 수량의 총합
# 판매년도    제품  
#    2013  무김치     420750
#         열무김치    419045
#         총각김치    483735
#    2014  무김치     447768
#         열무김치    489359
#         총각김치    551613
#    2015  무김치     540809
#         열무김치    601661
#         총각김치    742150
#    2016  무김치     733437
#         열무김치    637934
#         총각김치    634155
# Name: 수량, dtype: int64

df1.unstack(level=0) # 상위 레벨(연도)을 기준으로, default
# 판매년도    2013    2014    2015    2016
# 제품                                  
# 무김치    420750  447768  540809  733437
# 열무김치  419045  489359  601661  637934
# 총각김치  483735  551613  742150  634155

df1.unstack(level=1) # 하위 레벨(제품)을 기준으로
# 제품       무김치    열무김치    총각김치
# 판매년도                        
# 2013      420750     419045     483735
# 2014      447768     489359     551613
# 2015      540809     601661     742150
# 2016      733437     637934     634155

df2 = df1.unstack()
df2.stack()
# stack과 unstack은 반대의 역할을 수행하므로, 한번씩 실행하면 원본과 같은 결과
# 판매년도    제품  
#    2013  무김치     420750
#         열무김치    419045
#         총각김치    483735
#    2014  무김치     447768
#         열무김치    489359
#         총각김치    551613
#    2015  무김치     540809
#         열무김치    601661
#         총각김치    742150
#    2016  무김치     733437
#         열무김치    637934
#         총각김치    634155
# dtype: int64

```

# 15.3. pivot table

- 데이터에서 원하는 값을 뽑아 교차표를 작성한다.

```python
kimchi.pivot_table(index = '판매월',       # index 방향에 배치할 컬럼명
                   columns = '판매처',     # column 방향에 배치할 컬럼명
                   values = '수량',        # 교차표에 작성할 값을 갖는 컬럼
                   aggfunc = 'sum')        # 값에 적용할 그룹 함수

kimchi.pivot_table(index = '판매년도', columns = '제품', values = '판매금액', aggfunc = 'sum')
# index를 판매년도, column을 제품, 값은 판매금액의 총 합을 가지는 교차표 작성
# 제품           무김치       열무김치       총각김치
# 판매년도                                    
#    2013   3809133886     3416217894     4186789117
#    2014   4111403907     4392490590     5250364301
#    2015   5212738410     5859079408     7485159996
#    2016   6903506142     6627888927     6378374872
```