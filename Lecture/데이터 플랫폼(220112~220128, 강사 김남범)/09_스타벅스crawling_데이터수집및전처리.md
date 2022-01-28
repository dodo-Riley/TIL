# 9. 스타벅스 crawling_데이터 수집 및 전처리

- 라이브러리 및 모듈 호출
    
    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from bs4 import BeautifulSoup
    from selenium.webdriver.common.by import By
    import pandas as pd
    import numpy as np
    import time
    from tqdm.notebook import tqdm
    ```
    
- 드라이버 실행 및 페이지 다운로드
    
    ```python
    url = 'https://www.starbucks.co.kr/store/store_map.do?disp=locale'
    driver.get(url)
    
    seoul_btn = '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'
    driver.find_element(By.CSS_SELECTOR, seoul_btn).click()
    
    all_btn = '#mCSB_2_container > ul > li:nth-child(1) > a'
    driver.find_element(By.CSS_SELECTOR, all_btn).click()
    
    time.sleep(2) # 페이지 로딩 대기시간
    
    html = driver.page_source
    ```
    
- 파싱 및 필요 데이터 추출
    
    ```python
    soup = BeautifulSoup(html, 'html.parser') # 파싱
    
    store_data = [] # 데이터 리스트 초기화
    
    for store in tqdm(store_list): # 데이터 추출(진행상황 확인)
        name = store.select('li.quickResultLstCon>strong')[0].text.strip()
        long = store['data-long'] # 속성 값으로 추출
        lat = store['data-lat']
        store_type = store.select('i')[0]['class'][0][4:]
        tel = str(store.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]
        # tel = store.select('p,result_details')[0].text[-9:] 도 가능
        address = str(store.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
        # address = store.select('p,result_details')[0].text[:-9] 도 가능
        store_data.append([name, lat, long, store_type, address, tel])
    
    # address = store.select('li.quickResultLstCon>p,result_details')[0].text.split(')')[0]+')'
    # tel = store.select('li.quickResultLstCon>p,result_details')[0].text.split(')')[1]
    # 이 방법은 불가능, 데이터 중에 ()위치가 다른 것들이 존재
    
    # 엑셀 파일로 저장
    columns = ['매장명','위도','경도','매장타입','주소','전화번호']
    seoul_sb_df = pd.DataFrame(store_data, columns = columns)
    seoul_sb_df.to_excel('./seoul_sb_list_class.xlsx', index=False)
    ```
    
- 여러 데이터에서 시군구명과 필요 데이터만 추출
    - report.txt(시군구별 인구수 데이터)
        
        ```python
        sgg_pop_df = pd.read_csv('./files/report.txt', sep='\t', header=[2])
        columns = {'기간' : 'term',
                  '자치구' : 'city',
                  '세대' : 'household',
                  '계' : 'total_t',
                  '남자' : 'm_t',
                  '여자' : 'f_t',
                   '계.1' : 'total_k',
                  '남자.1' : 'm_k',
                  '여자.1' : 'f_k',
                   '계.2' : 'total_f',
                  '남자.2' : 'm_f',
                  '여자.2' : 'f_f',
                  '세대당인구' : 'population_per_hh',
                  '65세이상고령자' : '65_senior'}
        sgg_pop_df.rename(columns = columns, inplace=True)
        condition = sgg_pop_df['city']!='합계'
        sgg_pop_df_selected = sgg_pop_df[condition]
        sgg_pop_df_final = sgg_pop_df_selected[['city','total_t']]
        sgg_pop_df_final.columns = ['시군구명','주민등록인구']
        sgg_pop_df_final.to_excel('./sgg_pop_df_final_class.xlsx', index=False)
        ```
        
    
    - report2.txt(시군구별 사업체 종사자주 데이터) : 교재처럼 굳이 컬럼명을 바꿀 필요성을 느끼지 못해 바로 진행
        
        ```python
        sgg_biz_df = pd.read_csv('./files/report2.txt', sep=('\t'), header=2)
        sgg_biz_df_selected = sgg_biz_df[sgg_biz_df['동']=='소계']
        sgg_biz_df_final = sgg_biz_df_selected[['자치구','사업체수','계']]
        sgg_biz_df_final.columns = ['시군구명','사업체수','종사자수']
        sgg_biz_df_final.to_excel('./sgg_biz_df_final_class.xlsx', index=False)
        ```
        
    - seoul_sb_list_class.xlsx(서울 내 스타벅스 관련 정보 데이터)
        
        ```python
        seoul_sb_list = pd.read_excel('./seoul_sb_list_class.xlsx')
        sgg_names = []
        for address in seoul_sb_list['주소']:
            name = address.split()[1]
            sgg_names.append(name)
        seoul_sb_list['시군구명']=sgg_names # 기존 데이터에 시군구명 컬럼 추가
        seoul_sb_list.to_excel('./seoul_sb_list_final_class.xlsx', index=False)
        ```
        
- 여러 데이터를 시군구명을 기준으로 병합
    
    ```python
    seoul_sb_list = pd.read_excel('./seoul_sb_list_final_class.xlsx')
    sgg_pop = pd.read_excel('./sgg_pop_df_final_class.xlsx')
    sgg_biz = pd.read_excel('./sgg_biz_df_final_class.xlsx')
    sgg_list = pd.read_excel('./files/seoul_sgg_list.xlsx')
    
    # 직접 진행한 코드(value_counts() 사용)
    seoul_sb_list_sgg = pd.DataFrame(seoul_sb_list['시군구명'].value_counts())
    seoul_sb_list_sgg.columns=['매장수']
    
    seoul_sb_sgg_final = pd.merge(sgg_list, seoul_sb_list_sgg, how='left', left_on='시군구명', right_index=True)
    seoul_sb_sgg_final = pd.merge(seoul_sb_sgg_final, sgg_pop, how='left', on='시군구명')
    seoul_sb_sgg_final = pd.merge(seoul_sb_sgg_final, sgg_biz, how='left', on='시군구명')
    seoul_sb_sgg_final.to_excel('./seoul_sb_sgg_final_class.xlsx', index=False)
    
    # 교재와 같은 방식 코드(pivot_table()사용)
    seoul_sb_list_pivot = seoul_sb_list.pivot_table(index='시군구명',values='매장명',aggfunc='count')
    seoul_sb_list_pivot.rename(columns={'매장명':'매장수'}, inplace=True)
    
    seoul_sb_sgg_final = pd.merge(sgg_list, seoul_sb_list_pivot, how='left', on='시군구명')
    seoul_sb_sgg_final = pd.merge(seoul_sb_sgg_final, sgg_pop, how='left', on='시군구명')
    seoul_sb_sgg_final = pd.merge(seoul_sb_sgg_final, sgg_biz, how='left', on='시군구명')
    seoul_sb_sgg_final
    ```