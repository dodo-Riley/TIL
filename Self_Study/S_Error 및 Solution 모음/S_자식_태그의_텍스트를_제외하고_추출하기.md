# 자식 태그의 텍스트를 제외하고 추출하기

### 1. 상황

> 웹 크롤링을 통해 대그 내 텍스트를 추출하던 중, 부모 태그외에 자식태그 내 텍스트까지 추출되는 문제로 원하는 데이터가 얻어지지 않음
> 

### 2. 원인

> `.text`는 해당 태그 내 모든 텍스트를 추출하기 때문
> 

### 3. 해결책

> 텍스트 추출 전, `decompose()`를 통해 자식 태그 제거 후 텍스트 추출
> 

### 4. decompose()

> 특정 태그를 제거하고 `None`을 반환
> 

### 5. 해결 후 코드

```python
# 지니 차트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

service = Service('../chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=service)

url_1 = 'https://www.genie.co.kr/chart/top200'
url_2 = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220113&hh=13&rtm=Y&pg=2'

driver.get(url_1)
html_genie_1 = driver.page_source
soup_genie_1 = BeautifulSoup(html_genie_1, 'html.parser')
songs_data_ginie_1 = soup_genie_1.select('table.list-wrap>tbody>tr')

driver.get(url_2)
html_genie_2 = driver.page_source
soup_genie_2 = BeautifulSoup(html_genie_2, 'html.parser')
songs_data_ginie_2 = soup_genie_2.select('table.list-wrap>tbody>tr')

song_data_genie = []

for song in songs_data_ginie_1:
    rank = song.select_one('td.number')
    rank.span.decompose()
    rank_text = rank.text.strip()
    title = song.select('td.info > a.title.ellipsis')[0].text.strip()
    singer = song.select('td.info > a.artist.ellipsis')[0].text
    song_data_genie.append(['genie', rank_text, title, singer])
    
for song in songs_data_ginie_2:
    rank = song.select_one('td.number')
    rank.span.decompose()
    rank_text = rank.text.strip()
    title = song.select('td.info > a.title.ellipsis')[0].text.replace('19금','').strip()
    singer = song.select('td.info > a.artist.ellipsis')[0].text
    song_data_genie.append(['genie', rank_text, title, singer])

print(song_data_genie)
```

### 5. 출처 및 참고

- [https://stackoverflow.com/questions/24971962/python-beautifulsoup4-decompose-isnt-working](https://stackoverflow.com/questions/24971962/python-beautifulsoup4-decompose-isnt-working)