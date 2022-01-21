# 13. 다나와 crawling_데이터 시각화

- 라이브러리 및 모듈 호출
    
    ```python
    from matplotlib import font_manager, rc
    import matplotlib.pyplot as plt
    import seaborn as sns
    import platform 
    import pandas as pd
    import numpy as np
    ```
    
- 데이터 준비
    
    ```python
    pd_data_final = pd.read_excel('./cordless_final_class.xlsx')
    
    chart_data = pd_data_final.dropna(axis = 0) # 데이터 중 None 값이 있는 행은 삭제
    
    power_max_value = chart_data['흡입력'].max()
    power_mean_value = chart_data['흡입력'].mean()
    use_time_max_value = chart_data['사용시간'].max()
    use_time_mean_value = chart_data['사용시간'].mean()
    ```
    
- 산점도 그리기(seaborn 활용)
    
    ```python
    rc('font', family = 'Malgun Gothic')
    plt.figure(figsize=(20, 10))
    plt.title("무선 핸디/스틱청소기 차트")
    sns.scatterplot(x = '흡입력', # x축으로 사용할 데이터의 컬럼명
    								y = '사용시간', # y축으로 사용할 데이터의 컬럼명
    								size = '가격', # dot 크기로 사용할 데이터의 컬럼명(가격 값에 따라)
    								hue = chart_data['회사명'], # dot 색상(회사명 값에 따라)
    	              data = chart_data, # 사용할 데이터
    								sizes = (10, 1000), # dot의 크기 영역, seaborn에서는 이 영역 내에서 size 값이 정규화됨
    								legend = False) # 범례 미표시
    
    # 평균값과 최대값을 사용해 기준선 표시해주기
    plt.plot([0, power_max_value], # x축 데이터
              [use_time_mean_value, use_time_mean_value], # y축 데이터 
              'r--', # 선 모양
              lw = 1 ) # 선 두께
    plt.plot([power_mean_value, power_mean_value], 
              [0, use_time_max_value], 
              'r--', 
              lw = 1 )
    
    plt.show()
    
    ```
    
    - 기준선을 그리는 다른 방법
        
        ```python
        # 수평방향
        plt.hlines(use_time_mean_value, # 사용 값
        					 0, 400, # 범위
        						color='red', linestyle='dashed', linewidth=1)
        # 수직방향
        plt.vlines(power_mean_value, 0, 400, color='red', linestyle='dashed', linewidth=1)
        ```
        
    - dot에 이름 표시 하기
        
        ```python
        chart_data_selected = chart_data[:20] # 위에서 20개의 데이터만 추출
        
        plt.figure(figsize=(20, 10))
        plt.title("무선 핸디/스틱청소기 차트 상위 20")
        sns.scatterplot(x = '흡입력', y = '사용시간', size = '가격', hue = chart_data_selected['회사명'], 
                     data = chart_data_selected, sizes = (100, 2000), legend = False)
        plt.plot([0, power_max_value], 
                  [use_time_mean_value, use_time_mean_value], 
                  'r--', 
                  lw = 1 )
        plt.plot([power_mean_value, power_mean_value], 
                  [0, use_time_max_value], 
                  'r--', 
                  lw = 1 )
        
        for index, row in chart_data_selected.iterrows():
            x = row['흡입력']
            y = row['사용시간']
            s = row['제품명'].split(' ')[0]
            plt.text(x, y, s, size=20)
        
        # iterrows() 메소드는, 데이터프레임을 받아 해당 데이터프레임의 (인덱스, 행 내용(시리즈형태))을 반환
        
        plt.show()
        ```