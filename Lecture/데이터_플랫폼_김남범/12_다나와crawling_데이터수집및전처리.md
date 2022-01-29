# 12. 다나와 crawling_데이터 수집 및 전처리

- 라이브러리 및 모듈 호출
    
    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from bs4 import BeautifulSoup
    import time
    import pandas as pd
    import numpy as np
    from tqdm.notebook import tqdm
    ```
    
- 드라이버 실행 및 웹 페이지 다운로드
    
    ```python
    service = Service('../chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    url = 'http://search.danawa.com/dsearch.php?k1=무선청소기'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    ```
    
- 무선청소기에 대한 첫 번째 검색 결과 페이지에서 첫 제품 정보 추출
    
    ```python
    prod_items = soup.select('div.main_prodlist.main_prodlist_list>ul.product_list>li.prod_item')
    name = prod_items[0].select('p.prod_name')[0].text.strip()
    spec = prod_items[0].select('div.spec_list')[0].text.strip()
    price = prod_items[0].select('p.price_sect>a>strong')[0].text.strip().replace(',','')
    print(name,spec,price, sep='\n')
    
    # 원하는 데이터 추출 이상 없음 확인
    ```
    
- 원하는 검색어에 대한 url을 만들고 해당 검색어에 대한 제품 정보를 추출하는 함수 정의
    
    ```python
    # 검색어와 원하는 페이지 번호를 입력받아 해당 페이지의 주소를 반환
    def get_search_page_url(keyword, page):
        url = f'http://search.danawa.com/dsearch.php?query={keyword}&originalQuery={keyword}&volumeType=allvs&page={page}&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=102207&defaultPhysicsCategoryCode=72%7C80%7C81%7C0&defaultVmTab=2606&defaultVaTab=390042&tab=goods'
        return url
    
    # 접속한 페이지에서 제품 정보를 추출하고 리스트 형식으로 반환
    def get_prod_items(prod_items):
        prod_data = []
            
        for item in prod_items:
            if 'product-pot' in item['class']: # 제품 사이에 광고로 인한 불필요 정보에 대해서는 추출하지 않음
                continue
            try:
                name = item.select('p.prod_name')[0].text.strip()   
                spec = item.select('div.spec_list')[0].text.strip()
                price = item.select('p.price_sect>a>strong')[0].text.strip().replace(',','')
                prod_data.append([name,spec,price])      
    
            except:
                pass
          
        return prod_data
    ```
    
- ‘무선청소기’로 검색해 10페이지까지 크롤링하고 엑셀 파일로 저장
    
    ```python
    keyword = '무선청소기'
    total_page = 10
    prod_data_total = []
    
    for page in tqdm(range(1,total_page+1)): # 진행상황 확인하며 1페이지부터 10페이지까지 반복
        url = get_search_page_url(keyword, page)
        driver.get(url)
        time.sleep(2) # 페이지 로딩 시간 확보
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        prod_items = soup.select('div.main_prodlist.main_prodlist_list>ul.product_list>li.prod_item')
    
        prod_data = get_prod_items(prod_items) # 정보 추출
        
        prod_data_total = prod_data_total+prod_data # 모든 정보 리스트에 담기(append하면 3차원 리스트가되어 데이터를 다루기 불편해지므로 합연산 진행)
    
    data = pd.DataFrame(prod_data_total)
    data.columns = ['name','spec','price']
    data.to_excel('./cordless_data_class.xlsx', index=False)
    ```
    
- 크롤링한 데이터에서 원하는 정보만 추출
    - 회사명, 제품명
    
    ```python
    company_list = []
    product_list = []
    
    for name in data['name']:
        name_info = name.split(' ',1) # 공백을 기준으로 나누되, 가장 앞에서 첫 번째 공백에 대해서만 구분 진행
        company_name = name_info[0]
        product_name = name_info[1]
        
        company_list.append(company_name)
        product_list.append(product_name)
    ```
    
    - 제품 카테고리, 사용시간, 흡입력
    
    ```python
    category_list = []
    use_time_list = []
    power_list =[]
    
    for spec in data['spec']:
        spec_list = spec.split(' / ')
       
        category_name = spec_list[0]
        category_list.append(category_name)    
    
        for spec_info in spec_list:
            if '흡입력' in spec_info: # 값 내에 '흡입력' 문자열이 존재한다면
                power = spec_info.split(': ')[1]
            elif '사용시간' in spec_info: 
                use_time = spec_info.split(': ')[1]
            
        power_list.append(power)
        use_time_list.append(use_time)
    ```
    
    - 시간 및 흡입력 단위 통일
    
    ```python
    # 시간 단위 '분'으로 통일
    def convert_time_to_minute(time):
        try:
            if '시간' in time:
                hour = time.split('시간')[0]
                if '분' in time:
                    minute = time.split('시간')[-1].split('분')[0]
                else:
                    minute = 0
            else:
                hour = 0
                minute = time.split('분')[0]
            return int(hour)*60 + int(minute)
        
        except:
            return None # 특이한 형태의 경우 None 반환
        
    new_use_time_list = []
    
    for time in use_time_list:
        time_new = convert_time_to_minute(time)
        new_use_time_list.append(time_new)
    
    # 흡입력 단위 통일
    def get_power(power):
        try:
            power = power.upper()
            if 'W' in power:
                result = int(power.replace('A','').replace('W','').replace(',',''))
            elif 'PA' in power:
                result = int(power.replace('PA','').replace(',',''))/100
            else:
                result - None
            return result
        except:
            return None
    
    new_power_list = []
    for power in power_list:
        power_new = get_power(power)
        new_power_list.append(power_new)
    ```
    
- 처리가 끝난 필요 데이터만 모아서 데이터프레임 생성
    
    ```python
    pd_data = pd.DataFrame()
    pd_data['회사명'] = company_list
    pd_data['제품명'] = product_list
    pd_data['카테고리'] = category_list
    pd_data['흡입력'] = new_power_list
    pd_data['사용시간'] = new_use_time_list
    pd_data['가격'] = data['price'].astype('int')
    pd_data
    ```
    
- 카테고리가 ‘핸디/스틱청소기’인 데이터만 추출 및 저장
    
    ```python
    pd_data_final = pd_data[pd_data['카테고리']=='핸디/스틱청소기']
    pd_data_final.to_excel('./cordless_final_class.xlsx', index=False)
    ```
    
- 데이터 정렬
    
    ```python
    power_rank = pd_data_final.sort_values(by='흡입력', ascending=False)
    # 흡입력 컬럼 값을 기준으로 내림차순 정렬
    use_time_rank = pd_data_final.sort_values(by='사용시간', ascending=False)
    # 사용시간 컬럼 값을 기준으로 내림차순 정렬
    power_time_rank = pd_data_final.sort_values(by=['흡입력','사용시간'], ascending=False)
    # 흡입력을 1순위 기준으로, 사용시간을 2순위 기준으로 내림차순 정렬
    ```
    
- 가성비 청소기 찾기
    
    ```python
    condition = (pd_data_final['가격'] <= pd_data_final['가격'].mean()) & \
                (pd_data_final['사용시간'] >= pd_data_final['사용시간'].mean()) & \
                (pd_data_final['흡입력'] >= pd_data_final['흡입력'].mean())
    
    pd_data_final[condition]
    ```