# 15. 다나와 crawling_실습(ver.반복문 수정)

- 라이브러리 및 모듈 호출
    
    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from bs4 import BeautifulSoup
    import time
    import pandas as pd
    import numpy as np
    from tqdm.notebook import tqdm
    from matplotlib import font_manager, rc
    import matplotlib.pyplot as plt
    import seaborn as sns
    ```
    

- 첫 페이지에서 하나의 상품에 대해 진행하며 태그 찾기
    
    ```python
    service = Service('../chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    url = 'http://search.danawa.com/dsearch.php?k1=ssd&module=goods&act=dispMain'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    prod_items = soup.select('div.main_prodlist.main_prodlist_list>ul.product_list>li.prod_item')
    name = prod_items[0].select('p.prod_name')[0].text.strip()
    spec = prod_items[0].select('div.spec_list')[0].text.strip()
    price = prod_items[0].select('span.memory_price_sect')[0].text.strip()
    print(name,spec,price, sep='\n')
    ```
    

- 함수 정의
    
    ```python
    # url 만들기
    def get_search_page_url(keyword, page):
        url = f'http://search.danawa.com/dsearch.php?query={keyword}&originalQuery={keyword}&volumeType=allvs&page={page}&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=102207&defaultPhysicsCategoryCode=72%7C80%7C81%7C0&defaultVmTab=2606&defaultVaTab=390042&tab=goods'
        return url
    
    # 정보 추출
    def get_prod_items(prod_items):
        prod_data = []
            
        for item in prod_items:
            if 'product-pot' in item['class']:
                continue
            try:
                name = item.select('p.prod_name')[0].text.strip()   
                spec = item.select('div.spec_list')[0].text.strip()
                price = item.select('span.memory_price_sect')[0].text.strip().replace(',','')
                prod_data.append([name,spec,price])      
    
            except:
                pass
                
        return prod_data
    ```
    
- 크롤링 진행
    
    ```python
    keyword = '내장 ssd'
    total_page = 10
    prod_data_total = []
    
    for page in tqdm(range(1,total_page+1)):
        url = get_search_page_url(keyword, page)
        driver.get(url)
        time.sleep(2)
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        prod_items = soup.select('div.main_prodlist.main_prodlist_list>ul.product_list>li.prod_item')
    
        prod_data = get_prod_items(prod_items)
        
        prod_data_total = prod_data_total+prod_data
    
    data = pd.DataFrame(prod_data_total)
    data.columns = ['name','spec','price']
    data.to_excel('./ssd_data.xlsx', index=False)
    ```
    
- **데이터 전처리(수정 부분)**
    
    ```python
    company_list = []
    product_list = []
    category_list = []
    system_list = []
    write_list = []
    read_list =[]
    price_list = []
    
    for i in range(len(data)):
        
        if 'Western Digital' in data.loc[i][0]:
            name_info = data.loc[i][0].split(' ',2)
            company_name = name_info[0]+name_info[1]
            product_name = name_info[2]
        else:
            name_info = data.loc[i][0].split(' ',1)
            company_name = name_info[0]
            product_name = name_info[1]
            
        company_list.append(company_name)
        product_list.append(product_name)
        category_list.append(category_name)    
        system_list.append(system_name)
    
        spec_list = data.loc[i][1].split(' / ')
        category_name = spec_list[0]
        system_name = spec_list[2].split(' (')[0]
        
        if '순차읽기' not in data.loc[i][1]: # 데이터 중 아예 없는 경우
            read_list.append(None)
        
        if '순차쓰기' not in data.loc[i][1]:
            write_list.append(None)
        
        for spec in spec_list:
            if '순차읽기' in spec:
                try:
                    read = int(spec.split(': ')[1].split('M')[0].replace(',',''))
                    read_list.append(read)
                except:
                    read_list.append(None)  
    
            
            elif '순차쓰기' in spec:
                try:
                    write = int(spec.split(': ')[1].split('M')[0].replace(',',''))
                    write_list.append(write)
                except:
                    write_list.append(None)  
    
        
        try:
            price = int(data.loc[i][2].split('원')[0].replace(',',''))
            price_list.append(price)
        except:
            price_list.append(None)
    ```
    
- 데이터프레임 생성 및 값 처리
    
    ```python
    pd_data = pd.DataFrame()
    pd_data['회사명'] = company_list
    pd_data['제품명'] = product_list
    pd_data['카테고리'] = category_list
    pd_data['방식'] = system_list
    pd_data['순차쓰기(MB/s)'] = write_list
    pd_data['순차읽기(MB/s)'] = read_list
    pd_data['가격(원/1GB)'] = price_list
    pd_data.to_excel('./sdd_final_2.xlsx', index=False)
    
    ssd_final = pd_data.dropna(axis = 0)
    
    write_max_value = ssd_final['순차쓰기(MB/s)'].max()
    write_mean_value = ssd_final['순차쓰기(MB/s)'].mean()
    read_max_value = ssd_final['순차읽기(MB/s)'].max()
    read_mean_value = ssd_final['순차읽기(MB/s)'].mean()
    read_max_value
    ```
    
- 산점도 그리기 : 결과는 `14. 다나와 crawling_실습`과 동일함
    
    ```python
    rc('font', family = 'Malgun Gothic')
    
    plt.figure(figsize=(20, 10))
    plt.title("내장형 SSD 읽기/쓰기 속도 산점도")
    sns.scatterplot(x = '순차읽기(MB/s)', y = '순차쓰기(MB/s)', size = '가격(원/1GB)', hue = ssd_final['회사명'], 
                 data = ssd_final, sizes = (10, 1000), legend = False)
    plt.hlines(write_mean_value, 0, 6900, color='red', linestyle='dashed', linewidth=1)
    plt.vlines(read_mean_value, 0, 7400, color='red', linestyle='dashed', linewidth=1)
    plt.show()
    ```