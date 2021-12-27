# map과 apply, applymap

# 1. map 메소드

- `Series`를 인수로 받아 `Series`로 반환
    
    ```python
    import pandas as pd
    import numpy as np
    from pandas import Series, DataFrame
    
    f1 = lambda x: x**2
    df = DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns = ['a','b','c'], index=['A','B','C']) 
    df['a'].map(f1)
    # A     1
    # B    16
    # C    49
    # Name: a, dtype: int64
    df['A'].map(f1)
    # error
    # 데이터프레임의 컬럼에 해당하는 배열만 series로 인식 
    ```
    

# 2. apply 메소드

- `DataFrame`의 각 행 또는 열 단위를 인수로 받아 `Series`로 반환
    
    ```python
    df.apply(f1, axis=0)
    #     a   b   c
    # A   1   4   9
    # B  16  25  36
    # C  49  64  81
    df.apply(f1, axis=1)
    
    df['a'].apply(f1) # 가능
    ```
    

# 3. applymap 메소드

- `DataFrame`의 각 요소를 인수로 받아 `DataFrame`으로 반환
    
    ```python
    df.applymap(f1)
    #     a   b   c
    # A   1   4   9
    # B  16  25  36
    # C  49  64  81
    
    ```
    

> 출처 및 참고
> 
- [https://m.blog.naver.com/sienjing/221740320917](https://m.blog.naver.com/sienjing/221740320917)
- [https://kimdingko-world.tistory.com/164](https://kimdingko-world.tistory.com/164)