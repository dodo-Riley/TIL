# 1. 데이터 분석 기초_Pandas 기초

- 엑셀 파일 읽어오기
    
    ```python
    import pandas as pd
    import numpy as np
    
    sample_1 = pd.read_excel('./files/sample_1.xlsx',
                             header=1, # 헤더로 읽을 행 위치 인덱스
                             usecols='A:C', # 읽어올 열 선택
                             skipfooter=2 # 아래에서부터 스킵할 행 수
                             # names=['A','B','C'],  # 열 이름 재설정
                             # dtype = {'입국객수':np.float64} # 데이터타입 변경
                             ) 
    sample_1.dtypes # 각 열의 데이터 타입 확인
    ```
    
- 웹 상의 csv 파일 읽어오기
    
    ```python
    fish = pd.read_csv('https://bit.ly/fish_csv',
                       encoding = 'utf-8') # 종종 한글이 깨지면 encoding='euc-kr'
    ```
    
- 데이터 확인하기
    
    ```python
    sample_1.head() # 데이터의 가장 앞 5개의 행
    sample_1.tail() # 데이터의 가장 마지막 5개의 행
    
    sample_1.info() # 데이터의 간단한 정보 확인
    type(sample_1) # 데이터의 타입 확인
    sample_1.index # 인덱스 레인지 확인
    sample_1.columns # 열 확인
    sample_1.dtypes # 각 열 데이터 타입 확인
    
    sample_1.describe() # 데이터의 요약 통계량 확인(연속형 데이터)
    sample_1['성별'].value_counts() # '성별' 열의 통계량(이산형/범주형 데이터)
    ```
    
- 인덱싱
    
    ```python
    sample_1['입국객수']
    sample_1[['국적코드', '성별']] # 열 인덱싱
    
    sample_1['기준년월'] = '2019-11' # 새로운 열 생성
    
    condition = sample_1['성별']=='남성' 
    sample_1[condition] # 조건에 해당하는 행 추출
    sample_1[~condition] # 조건을 만족하지 않는 행 추출
    
    condition_1 = sample_1['성별']=='남성'
    condition_2 = sample_1['입국객수']>=150000
    sample_1[condition_1 & condition_2] # 두 조건을 모두 만족하는 행 추출
    sample_1[condition_1 | condition_2] # 두 조건 중 하나라도 만족하는 행 추출
    
    condition = (sample_1['국적코드']=='A01') | (sample_1['국적코드']=='A18')
    condition = (sample_1['국적코드'].isin(['A01', 'A18'])) # 같은 결과 반환, 국적코드 열에 A01이나 A18이 있으면 해당 행 출력
    
    sample_1.loc[1:3, '성별'] # 인덱스는 1부터 3까지, 열은 성별인 데이터 출력
    ```
    
- 데이터프레임 병합
    
    ```python
    code_master = pd.read_excel('./files/sample_codemaster.xlsx',header=0,usecols='A:B',skipfooter=0)
    
    # 옆으로 병합, merge
    sample_1_code = pd.merge(left = sample_1, # 왼쪽에 붙일 데이터
                            right = code_master, # 오른쪽에 붙일 데이터
                            how='left', # 붙이는 방법(왼쪽 데이터에 있는 데이터를 기준) # inner는 NaN이 있게되면 아예 삭제, outer 전부 나옴
                            left_on = '국적코드', # 왼쪽 데이터의 기준 열 제목
                            right_on = '국적코드') # 오른쪽 데이터의 기준 열 제목
    
    # 위아래로 병합, append
    sample_2 = pd.read_excel('./files/sample_2.xlsx', header=1, skipfooter=2, usecols='A:C')
    sample_2['기준년월'] = '2019-12'
    sample_2_code = pd.merge(left=sample_2, right=code_master, how='left', left_on='국적코드',right_on='국적코드')
    sample = sample_1_code.append(sample_2_code, # 아래에 붙일 데이터
                                  ignore_index = True) # 기존 인덱스 무시하고 순차적으로 새로 부여
    
    # concat
    sample_concat = pd.concat([sample_1_code, sample_2_code], # 합칠 데이터
                            ignore_index = True, # 기존 인덱스 무시
                             axis = 0) # 행 기준(세로방향)으로 병합
    ```
    
- 엑셀 파일로 저장하기
    
    ```python
    sample.to_excel('./files/sample_class.xlsx', # 저장 위치 및 파일명
                    index=False, # 인덱스 삭제
                    na_rep='NaN', # NaN 표시(안하면 공백으로 저장됨)
                    sheet_name='mysheet') # 시트 이름 설정
    
    # 하나의 파일에 여러개의 시트 생성
    with pd.ExcelWriter('./files/multiple_sheet.xlsx') as writer:
        sample.to_excel(writer, sheet_name = 'sheet_1')
        sample_1_code.to_excel(writer, sheet_name = 'sheet_2', index=False, na_rep='NaN')
    ```
    
- Pivot table과 groupby
    
    ```python
    sample_pivot = sample.pivot_table(values='입국객수', # 값으로 들어갈 데이터
                                     index='국적명', # 인덱스로 설정할 데이터
                                     columns='기준년월', # 열로 설정할 데이터
                                     aggfunc='mean') # # 값에 적용할 함수, default가 평균
    
    sample['입국객수'].mean()
    sample.groupby('성별').mean() # 성별에 따른 입국객수의 평균 값 반환
    ```
    
- 시각화
    
    ```python
    import matplotlib.pyplot as plt
    plt.rc('font', family='Malgun Gothic') # 한글 깨지지 않도록
    sample_pivot.plot(kind='bar', figsize=(10,8), rot=0) # 막대그래프 그리기
    plt.xlabel('')
    plt.xticks(size=15)
    plt.yticks(size=10)
    
    plt.show()
    ```