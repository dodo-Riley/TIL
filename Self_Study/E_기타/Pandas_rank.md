# Pandas_rank()

> 원하는 범위에서 값들의 크기 순위를 계산한다.
> 
- 기본 구조
    
    ```python
    DataFrame.rank(self, 
    		       axis = 0, # default는 0(index), 행 기준 순위 계산. 1이면 열 기준 
     method = 'average', # 동점자 처리법
    numeric_only = None, # True로 설정된 경우 숫자 열만 계산 
     na_option = 'keep', # NaN 값 순위를 매기는 방법
       ascending = True, # 오름차순, 내림차순 정렬 여부
        		pct = False) # 반환 된 순위를 백분위 수 형식으로 표시할지 여부
    ```
    

- 동점자 처리
    
    ```python
    # average: 그룹의 평균 순위 부여 (예: 두 명이 공동 1등이라면 둘 다 1.5등으로 처리)
    # min: 그룹에서 가장 낮은 순위 부여 (예: 두 명이 공동 1등이라면 둘 다 1등으로 처리)
    # max: 그룹에서 가장 낮은 순위 부여 (예: 두 명이 공동 1등이라면 둘 다 2등으로 처리)
    # first: 그룹에서 표시되는 순서대로 순위 부여 (예: 두 명이 공동 1등이라면 순서가 빠른 사람을 1등으로 처리)
    # dense: min과 동일함. 다만 순위는 항상 1씩 증가
    
    df = DataFrame([23,25,56,55,23])
    df['rank_average'] = df[0].rank(method='average')
    df['rank_min'] = df[0].rank(method='min')
    df['rank_max'] = df[0].rank(method='max')
    df['rank_first'] = df[0].rank(method='first')
    df['rank_dense'] = df[0].rank(method='dense')
    
    #    0  rank_average  rank_min  rank_max  rank_first  rank_dense
    #0  23           1.5       1.0       2.0         1.0         1.0
    #1  25           3.0       3.0       3.0         3.0         2.0
    #2  56           5.0       5.0       5.0         5.0         4.0
    #3  55           4.0       4.0       4.0         4.0         3.0
    #4  23           1.5       1.0       2.0         2.0         1.0
    ```
    
- 오름차순/내림차순
    
    ```python
    # ascending=True는 오름차순
    # ascending=False는 내림차순
    
    df2 = DataFrame()
    df2['오름차순'] = df[0].rank(ascending=True)
    df2['내림차순'] = df[0].rank(ascending=False)
    
    #   오름차순  내림차순
    # 0     1.5      4.5
    # 1     3.0      3.0
    # 2     5.0      1.0
    # 3     4.0      2.0
    # 4     1.5      4.5
    ```
    

- NaN 값 처리
    
    ```python
    # keep: 기본 값으로 NaN의 순위에 NaN을 부여
    # top: 그룹에서 가장 높은 순위 부여
    # bottom: 그룹에서 가장 높은 순위 부여
    
    df3 = DataFrame([1,2,3,4,np.nan])
    df3['keep'] = df3[0].rank(na_option = 'keep')
    df3['top'] = df3[0].rank(na_option = 'top')
    df3['bottom'] = df3[0].rank(na_option = 'bottom')
    
    #      0  keep  top  bottom
    # 0  1.0   1.0  2.0     1.0
    # 1  2.0   2.0  3.0     2.0
    # 2  3.0   3.0  4.0     3.0
    # 3  4.0   4.0  5.0     4.0
    # 4  NaN   NaN  1.0     5.0
    ```
    

> 출처 및 참고 : [https://hogni.tistory.com/48](https://hogni.tistory.com/48)
>