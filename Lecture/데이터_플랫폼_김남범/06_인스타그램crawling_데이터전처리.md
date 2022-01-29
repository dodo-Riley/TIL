# 6. 인스타그램 crawling

## 6.1. 인스타그램에서 데이터 crawling하기

- 사용할 라이브러리 및 모듈 호출
  
    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as py
    import time
    import unicodedata
    import re
    from selenium.webdriver.common.by import By\
    from collections import Counter
    ```
    
- 드라이버 실행 및 페이지 접속
    - 교재에서는 코드를 통해 로그인을 처리했지만, 계정정보 보안 문제로 직접 로그인
    
    ```python
    service = Service('../chromedriver/chromedriver.exe')
    driver=webdriver.Chrome(service=service)
    
    url = 'https://www.instagram.com/'
    driver.get(url)
    time.sleep(3) # 페이지 로딩에 걸리는 시간 때문에 대기시간 부여
    ```
    
- 원하는 태그를 검색한 페이지 접속
  
    ```python
    def insta_searching(word):
        url = f'https://www.instagram.com/explore/tags/{word}/'
        return url
    
    word = '제주도맛집'
    url = insta_searching(word)
    driver.get(url)
    time.sleep(5)
    ```
    
- 실제 crawling 진행할 내용이 있는 페이지로 가서 필요 내용 추출
  
    ```python
    def select_first(driver):
        first = driver.find_element(By.CSS_SELECTOR, 'div._9AhH0')
        first.click()
        time.sleep(3)
        
    select_first(driver) # 추출할 첫 페이지로 접속
    
    html = driver.page_source # 페이지 다운로드
    soup = BeautifulSoup(html, 'html.parser') # 파싱
    
    # 내용 추출
    content = soup.select('.C4VMK>span')[0].text
    
    # tag 추출
    tags = re.findall(r'#[^\s#,\\]+', content)
    # 정규표현식. content 중 #으로 시작하고, 공백(\s)/#/,/\가 아닌 경우를 찾아 리스트 형태로 저장
    
    # 날짜 추출
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10] # 속성값 추출로 진행
    
    # 좋아요 수 추출
    like = soup.select('a.zV_Nj > span')[0].text
    
    # 위치정보 추출
    place = soup.select('a.O4GlU')[0].text
    ```
    
- 첫 페이지를 마치고 다음 페이지로 이동
  
    ```python
    def move_next(driver):
        right = driver.find_element(By.CSS_SELECTOR, 'div.l8mY4.feth3')
        right.click()
        time.sleep(2)
        
    move_next(driver)
    ```
    
- 내용을 추출하는 부분을 함수로 정의하고, 크롤링 함수 만들기
  
    ```python
    # [사용 라이브러리 및 모듈 호출]
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as py
    import time
    import unicodedata
    import re
    from selenium.webdriver.common.by import By
    
    # [함수 정의]
    # 원하는 태그로 검색한 페이지 url 설정 함수
    def insta_searching(word):
        url = f'https://www.instagram.com/explore/tags/{word}/'
        return url
    
    # 해당 검색 결과 페이지에서 첫 페이지 접속 함수
    def select_first(driver):
        first = driver.find_element(By.CSS_SELECTOR, 'div._9AhH0')
        first.click()
        time.sleep(3)
     
    # 접속한 페이지의 내용을 추출하는 함수   
    def get_content(driver):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # 실제 페이지에서는 원하는 내용이 없는 경우도 존재하기 때문에 except문 사용
        try:
            content = soup.select('.C4VMK>span')[0].text
    				# content = unicodedata.normalize('NFC', content)
    				# mac 환경에서는 한글 자음과 모음이 분리되어 나오는 현상이 있으므로, 이를 방지하기위해 위 코드를 추가하면됨
        except:
            content=''
        
        tags = re.findall(r'#[^\s#,\\]+', content)
        
        date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    
        try:
            like = soup.select('a.zV_Nj > span')[0].text
        except:
            like = 0
            
        try:
            place = soup.select('a.O4GlU')[0].text
        except:
            place = ''
            
        data = [content, date, like, place, tags]
        
        return data
    
    # 하나의 페이제에서 추출이 종료된 후 다음 페이지로 이동하는 함수
    def move_next(driver):
        right = driver.find_element(By.CSS_SELECTOR, 'div.l8mY4.feth3')
        right.click()
        time.sleep(2)
    
    # 크롤링 자동화 함수, word는 검색 태그, target은 크롤링할 페이지 수
    def insta_crawling(word,target):
        url = insta_searching(word)
        driver.get(url)
        time.sleep(5)
    
        select_first(driver) 
        
        for i in range(target):
            try:
                data = get_content(driver)
                result.append(data)
                move_next(driver)
            except:
                time.sleep(2)
                move_next(driver)
                
        return result
    
    # [초기값 설정]
    result = []
    
    # [메인 실행 코드] 
    insta_crawling('제주도맛집',10)
    ```
    
- 크롤링한 데이터 엑셀 파일로 저장
  
    ```python
    result_df = pd.DataFrame(result)
    result_df.columns = ['content', 'date', 'like', 'place', 'tags']
    result_df.to_excel('./files/1_crawling_jejudoMatJip.xlsx', index=False)
    ```
    

## 6.2. 데이터 전처리

- 크롤링한 데이터 합치기
  
    ```python
    jeju_insta_df = pd.DataFrame()
    
    f_list = ['1_crawling_jejudoMatJip.xlsx', '1_crawling_jejudoGwanGwang.xlsx', '1_crawling_jejuMatJip.xlsx', '1_crawling_jejuYeoHang.xlsx']
    
    for fname in f_list:
        fpath = f'./files/{fname}'
        temp = pd.read_excel(fpath)
        jeju_insta_df = jeju_insta_df.append(temp)
        
    jeju_insta_df.columns = ['content', 'date', 'like', 'place', 'tags']
    
    jeju_insta_df.shape # 제대로 합쳐졌는지 확인
    ```
    
- 병합 데이터에서 중복되는 데이터 제거 후 엑셀 파일로 저장
  
    ```python
    jeju_insta_df.drop_duplicates(subset=['content'], inplace=True)
    # 'content' 컬럼의 값을 기준으로 중복 행 제거, 수행 후 원본 변경
    jeju_insta_df.to_excel('./files/1_crawling_raw.xlsx', index=False)) # 이미 되어있는 파일 사용
    ```
    
- 태그 값 내 문자만 추출
  
    ```python
    raw_total = jeju_insta_df.copy() # 복사본을 새 변수에 저장
    raw_total.columns
    raw_total['tags'] # 데이터 확인
    
    tags_total = [] # 초기값 설정
    
    for tags in raw_total['tags']:
        tags_list = tags[3:-2].split("', '#") # 태그 컬럼의 값들을 #이나 공백, 그리고 ,등의 불필요 부분을 제거하고 문자만 추출
        for tag in tags_list:
            tags_total.append(tag)
    
    from collections import Counter
    
    tag_counts = Counter(tags_total) # 판다스의 value_counts와 비슷한 결과. 리스트 내의 요소와 횟수를 알려줌
    tag_counts.most_common(10) # 상위 10개 내용 반환
    ```
    
- 불용어(STOPWORDS) 설정 및 제거된 태그 값 목록 만들기
  
    ```python
    STOPWORDS = ['일상', '선팔', '제주도', 'jeju', '반영구', '제주자연눈썹',
    							'서귀포눈썹문신', '제주눈썹문신', '소통', '맞팔', '제주속눈썹', '제주일상','여행',
                 '눈썹문신','카멜리아힐','daily','제주반영구','제주남자눈썹문신','서귀포자연눈썹',
    						'서귀포남자눈썹문신','제주메이크업','서귀포반영구','서귀포속눈썹','셀카','제주속눈썹연장']
    
    tag_total_selected = []
    
    for tag in tags_total:
        if tag not in STOPWORDS:
            tag_total_selected.append(tag)
            
    tag_counts_selected = Counter(tag_total_selected)
    tag_counts_selected.most_common(50)
    ```
    
- tag_count_selected를 데이터프레임으로 만들고 공백 데이터 처리
  
    ```python
    tag_count_df = pd.DataFrame(tag_counts_selected.most_common(50))
    tag_count_df.columns = ['tag','count']
    
    tag_count_df['tag'].replace('',None,inplace=True) # tag 컬럼의 값이 공백이면 None으로 변경 
    tag_count_df.dropna(subset=['tag'], inplace=True) # None이 포함된 행 제거
    ```
    
