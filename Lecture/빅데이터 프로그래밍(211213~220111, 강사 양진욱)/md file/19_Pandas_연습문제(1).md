# 19. Pandas_연습문제(1)

# 19.1. 사용 데이터 확인

```python
run my_modules
import matplotlib.pyplot as plt
df1 = pd.read_csv('./data/cancer_test.csv')
df1.columns
df1.dtypes
df1.head()
[df1.info](http://df1.info/)()
df1.describe()
```

# 19.2. 문제

1. radius_mean, texture_mean, texture_se, smoothness_se에 대해 na인 행 제거한 후, 총 행의 수 반환
    
    ```python
    df1['radius_mean'].isnull().sum() # radius_mean 열에서 na인 값의 개수
    df1['texture_mean'].isnull().sum() # texture_mean 열에서 na인 값의 개수
    df1['texture_se'].isnull().sum() # texture_se 열에서 na인 값의 개수
    df1['smoothness_se'].isnull().sum() # smoothness_se 열에서 na인 값의 개수
    
    vbool = df1['radius_mean'].isnull() & df1['texture_mean'].isnull() & df1['texture_se'].isnull() & df1['smoothness_se'].isnull()
    vbool.sum() # 4개가 모두 na인 행의 개수
    
    df1.loc[vbool,:] # 4개가 모두 na인 행 색인
    
    df1.shape      # df1의 형태
    df1.shape[0]   # df1의 행 수
    df1.shape[1]   # df1의 열 수
    df1.shape[0]-vbool.sum() # not null 개수
    
    nrow = df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how ='all').shape[0]
    print(nrow)   # 답 : 565
    ```
    

1. concavity_mean의 standard scailing(표준화) 후, 결과가 0.1 이상인 값의 개수 출력
    
    ```python
    # standard scailing : (값-평균)/표준편차
    # minmax scailing = (값-최소)/(최대-최소)
    
    vscale = (df1['concavity_mean']-df1['concavity_mean'].mean())/df1['concavity_mean'].std()
    (vscale>0.1).sum()  # 답 207
    ```
    

1. texture_Se의 na를 제외한 상위 10% 값을 이상치로 가정한다. 10%를 제외한 값의 최대값으로 이상치를 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력
    
    ```python
    # NaN을 제외한 상위 10% 값의 순위 구하기
    nx = int(np.trunc(df1['texture_se'].dropna().shape[0] * 0.1)) # 56
    
    # 'texture_se' 열에서 값들을 내림차순으로 순위 정하기(값이 클수록 높은 순위)
    vrank = df1['texture_se'].rank(ascending = False, method='first')  # rank 함수 따로 정리할 것.
    
    # 정상치와 이상치 데이터 구분하기
    
    df1.loc[vrank>nx, 'texture_se']  
    # 상위 10%인 값의 순위보다 해당 값의 순위가 큰(값이 더 작은) 정상치 데이터
    df1.loc[vrank<=nx, 'texture_se']  
    # 10%인 값의 순위보다 낮은(값이 더 큰) 이상치 데이터
    
    # 10%를 제외한 값의 최대값 구하기
    vmax = df1.loc[vrank>nx, 'texture_se'].max() 
    
    # 이상치를 원하는 값으로 변경하기
    df1.loc[vrank<=nx, 'texture_se'] = vmax 
    
    # 평균 구하기
    mean_ = df1['texture_se'].mean()
    
    # 반올림하기
    round(mean_,2)
    
    # 답 : 1.17
    # print('%0.2f' % mean_) 쳐도 나옴
    ```
    

1.  symmetry_mean의 결측치를 최소값으로 수정한 후 평균을 소수점 둘째자리로 반올림해서 출력
    
    ```python
    df1['symmetry_mean'].min() # '-'가 존재해서 제대로 안나옴
    
    from numpy import nan as NA
    
    # 결측치를 NaN으로 변경
    df2 = df1['symmetry_mean'].replace(['-','.','pass'], NA)
    
    # 데이터를 실수형으로 변경
    df3 = df2.astype('float')
    
    # 최소값 구하지
    df3.min()
    
    # NaN을 최소값으로 변경
    df4 = df3.fillna(df3.min())
    
    # 원하는 값 출력
    print(round(df4.mean(),2))
    
    # 답 : 0.18
    ```