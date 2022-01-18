# 7. 인스타그램 crawling_데이터 시각화

> `6. 인스타그램 crawling_데이터 전처리`에서 처리한 데이터를 사용
> 

- 막대차트로 태그 값 그래프 그리기(seaborn 활용)
    
    ```python
    import matplotlib.pyplot as plt
    from matplotlib import rc
    import seaborn as sns
    
    rc('font', family='Malgun Gothic')
    
    plt.figure(figsize=(10,8))
    sns.barplot(x='count',y='tag', data=tag_count_df)
    plt.show()
    ```
    

- tag 값으로 wordcloud 그리기
    
    ```python
    from wordcloud import WordCloud
    
    font_path = 'C:/Windows/Fonts/malgun.ttf' # 한글 폰트 경로 지정
    wordcloud = WordCloud(font_path=font_path, # 폰트 경로
                         background_color='white', # 배경색
                         max_words=100, # 나타낼 최대 단어 개수
                         relative_scaling=0.3, # 단어들의 상대적인 크기, 0에 가까울수록 빈도수의 순위에 1에 가까울수록 빈도수에 더 큰 영향
                         width=800, # 이미지 너비
                         height=400 # 이미지 높이
    										).generate_from_frequencies(tag_counts_selected) # 사용 데이터 및 함수 적용
    plt.figure(figsize=(15,10))
    plt.imshow(wordcloud) # image를 보여줌
    plt.axis('off')
    # plt.savefig('./files/tag_wordcloud.png') 이미지 파일 저장하기
    ```
    
- 지도 시각화
    - 사용할 데이터 가져오기
        
        ```python
        import pandas as pd
        
        raw_total = pd.read_excel('./files/1_crawling_raw.xlsx')
        location_counts = raw_total['place'].value_counts()
        location_counts_df = pd.DataFrame(location_counts)
        locations = list(location_counts_df.index)
        ```
        
    - 카카오 API를 활용 장소 검색 및 전처리
        
        ```python
        import requests
        from tqdm.notebook import tqdm
        
        # 장소 검색 함수 정의
        def find_places(searching):
            # 접속 url
            url = f'https://dapi.kakao.com/v2/local/search/keyword.json?query={searching}'
        
            # headers 입력
            headers = {'Authorization' : 'KakaoAK aff5afbefd96a33de57ccdc57d7b6322'}
            
            # API 요청 및 정보 받기
            places = requests.get(url, headers = headers).json()['documents']
            
            # 필요정보 추출
            place = places[0] # 여러개의 장소 정보 중 첫 번째 데이터 저장
            name = place['place_name']
            x = place['x']
            y = place['y']
            data = [name, x, y, searching]
            
            return data # 장소의 이름과 위/경도, 그리고 검색에 사용한 이름을 요소로 가지는 리스트가 반환
        
        # 인스타그램에서 크롤링한 테이터에서 장소만 사용해 데이터 추출
        locs_inform = []
        
        for loc in tqdm(locations[:200]): # tqdm()을 통해 실시간 처리 상황 확인 가능
            try:
                data = find_places(loc)
                locs_inform.append(data)
                time.sleep(1)
            except:    # 장소가 없는 데이터의 경우 패스
                pass
        
        locs_inform_df = pd.DataFrame(locs_inform) # 추출한 데이터를 데이터프레임으로 변환
        locs_inform_df.columns=['name_official','경도','위도','name'] # 컬럼명 추가
        locs_inform_df.to_excel('./files/3_locations.xlsx', index=False) # 엑셀파일로 저장
        
        # 데이터 병합을 통해 공식 장소명과 위/경도, 등장 횟수 추출
        location_counts_df = pd.read_excel('./files/3_location_counts.xlsx', index_col = 0) # 첫 컬럼을 인덱스로 데이터 불러오기
        locations_inform_df = pd.read_excel('./files/3_locations.xlsx')
        location_data = pd.merge(locations_inform_df, 
        												location_counts_df, # 병합할 데이터
                                how = 'inner', # 양쪽에 모두 있는 데이터만 포함
        												left_on = 'name_official', # 왼쪽 데이터는 name_official 컬럼을 기준으로
        												right_index=True) # 오른쪽 데이터는 인덱스를 기준으로
        
        # 병합된 데이터에서 같은 장소명인 경우, 등장 횟수를 합치기
        location_data = location_data.pivot_table(index=['name_official','경도','위도'], values='place',aggfunc='sum')
        ```
        
    - 지도 시각화하기(folium 활용)
        
        ```python
        import folium
        
        Mt_Hanla = [33.362500, 126.533694] # 지도 중심으로 사용할 위/경도
        map_jeju = folium.Map(location = Mt_Hanla, zoom_start=10)
        
        # 타일 변경 (타일을 따로 설정하지 않을 경우, openstreetmap이 디폴트)
        folium.TileLayer('stamentoner').add_to(map_jeju)
        
        for i in range(len(location_data)):
            name = location_data['name_official'][i]
            count = location_data['place'][i]
            size = int(count)*2
            lat = float(location_data['경도'][i])
            long = float(location_data['위도'][i])
            folium.CircleMarker((long,lat), radius=size, color='red', popup=name).add_to(map_jeju)
        
        # html로 저장하기
        map_jeju.save('./files/3_jeju_class.html')
        ```
        
    - circlemarker끼리 그룹으로 표시하기
        
        ```python
        from folium.plugins import MarkerCluster
        
        locations = [] # 위도와 경도를 담을 리스트 초기화
        names = [] # 장소명을 담을 리스트 초기화
        
        for i in range(len(location_data)): # 모든 행에 대해서 위도와 경도, 장소명을 각 리스트에 추가
            data = location_data.iloc[i]
            locations.append([data['위도'], data['경도']])
            names.append(data['name_official'])
         
        # 바탕 지도 생성   
        Mt_Hanla = [33.362500, 126.533694]
        map_jeju_2 = folium.Map(location = Mt_Hanla, zoom_start=10)
        
        # 타일 레이어 설정
        tiles = ['stamenwatercolor', 'cartodbpositron', 
                 'openstreetmap', 'stamenterrain']
        
        for tile in tiles:
            folium.TileLayer(tile).add_to(map_jeju_2)
        
        # 그룹화된 마커 표시
        marker_cluster = MarkerCluster(locations = locations, popups=names, name='Jeju', overlay=True, control=True).add_to(map_jeju_2)
        folium.LayerControl().add_to(map_jeju_2)
            
        map_jeju_2.save('./files/3_jeju_cluster_class.html')
        ```
        
    
    - 참고 : folium 사용하기
        
        ```python
        import folium
        
        # 지도 중심으로 사용할 위도와 경도
        latitude = 37.394946
        longitude = 127.111104
        
        # 기본 바탕 지도 그리기
        m = folium.Map(location = [latitude, longitude], # 중심
                       width = 500, 
                       height = 300,
                       zoom_start = 10)
        
        # 마커 추가
        folium.Marker(location = [latitude, longitude],
                     popup = '판교역', # 클릭했을 때 뜨는 문자, 영상의 소스코드나 링크도 가능
                     tooltip = '판교역 입구', # 마우스 오버했을 때 뜨는 문자
                     icon = folium.Icon(color='red',icon_color='orange',icon='wifi',prefix='fa') # 마커 속성 변경(외부색상, 내부색상, 아이콘모양, 아이콘출처(fa는 font awesome))
                     ).add_to(m) # 그린 지도에 추가
        
        # 원형 마커 추가
        folium.CircleMarker(location = [latitude, longitude],
                           color = 'tomato',
                           radius = 50,
                           tooltip = '반경').add_to(m)
        ```