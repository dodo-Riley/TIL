# 11. 스타벅스 crawling_데이터 시각화

- 라이브러리 및 모듈 호출
    
    ```python
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import folium
    import json
    ```
    
- 사용할 데이터 불러오기
    
    ```python
    seoul_sb_sgg_final = pd.read_excel('./seoul_sb_sgg_final_class.xlsx') 
    # 옵션에 thousands=',' 넣으면 나중에 타입변경처리 불필요
    seoul_sb_list = pd.read_excel('./seoul_sb_list_final_class.xlsx')
    seoul_sgg_geo = json.load(open('./maps/seoul_sgg.geojson', encoding='utf-8'))
    ```
    
- 시군구별 스타벅스 매장 분포 시각화하기
    
    ```python
    sb_map = folium.Map(location = [37.573050, 126.979189],
                                    tiles = 'StamenTerrain',
                                    zoom_start = 11)
                                    
    for idx in seoul_sb_list.index:
        lat = seoul_sb_list.loc[idx, '위도']
        lng = seoul_sb_list.loc[idx, '경도']
        store_type = seoul_sb_list.loc[idx, '매장타입']
        names = seoul_sb_list.loc[idx, '매장명']
        address = seoul_sb_list.loc[idx, '주소']
        
    	  # 매장 타입에 따라 색상과 사이즈 설정
        fillColor = ''
        if store_type == 'general':
            fillColor = 'green'
        elif store_type == 'reserve':
            fillColor = 'blue'
        elif store_type == 'generalDT':
            fillColor = 'red'
        elif store_type == 'generalWT':
            fillColor = 'black'
        
        Radius = None
        if store_type == 'general':
            Radius = 3
        elif store_type == 'reserve':
            Radius = 5
        elif store_type == 'generalDT':
            Radius = 4
        elif store_type == 'generalWT':
            Radius = 7 
        
        folium.CircleMarker(location = [lat,lng],
                          color = fillColor,
                          radius = Radius,
                          weight = 1, # 외곽선 두께
                          fill = True, # 내부 채우기
                          fill_color = fillColor, # 내부 색상
                          fill_opacity = 1, # 내부 색상 투명도
                          popup = '<pre>'+address+'</pre>', # 팝업 내용 가로로(html 태그 사용, 나머지 볼드나 이탤릭 등 태그도 먹힘)
                          tooltip = '<b>'+names+'</b>').add_to(sb_map)
    
    sb_map
    ```
    
- 시군구별 경계선 및 구역 시각화하기
    
    ```python
    sb_bubble = folium.Map(location = [37.573050, 126.979189],
                          tiles = 'CartoDB positron',
                          zoom_start = 11)
    
    def style_function(feature):
        return {'opacity' : 0.7, # 선 투명도
                'weight' : 1, # 선 두께
                'color' : 'red', # 선 색상
               'fillOpacity' : 0.1, # 선으로 이루어진 내부 투명도 설정
               'dashArray' : '5,5',} # 점선의 간격 설정
    
    folium.GeoJson(seoul_sgg_geo,
                  style_function = style_function).add_to(sb_bubble)
    
    sb_bubble
    ```
    
- 서울시 스타벅스 매장 평균 수와 각 시군구별 매장 수를 비교해 버블맵 그리기
    
    ```python
    sb_bubble = folium.Map(location = [37.573050, 126.979189],
                          tiles = 'CartoDB positron',
                          zoom_start = 11)
    
    def style_function(feature):
        return {'opacity' : 0.7, # 선 투명도
                'weight' : 1, # 선 두께
                'color' : 'red', # 선 색상
               'fillOpacity' : 0.1, # 선으로 이루어진 내부 투명도 설정
               'dashArray' : '5,5',} # 점선의 간격 설정
    
    folium.GeoJson(seoul_sgg_geo,
                  style_function = style_function).add_to(sb_bubble)
    
    for idx in seoul_sb_sgg_final.index:
        lat = seoul_sb_sgg_final.loc[idx, '위도']
        lng = seoul_sb_sgg_final.loc[idx, '경도']
        names = seoul_sb_sgg_final.loc[idx, '시군구명']
        count = int(seoul_sb_sgg_final.loc[idx, '매장수'])
        
        fillColor = ''
        if count > seoul_sb_sgg_final['매장수'].mean(): # 매장수의 평균을 구하고 비교 
            fillColor = 'red'
        else:
            fillColor = 'blue' 
        
        folium.CircleMarker(location = [lat,lng],
                          color = 'gray',
                          radius = count/2,
                          weight = 2, # 외곽선 두께
                          fill = True, # 내부 채우기
                          fill_color = fillColor, # 내부 색상
                          fill_opacity = 1, # 내부 색상 투명도
                          tooltip = '<b>'+names+'</b>').add_to(sb_bubble)
    
    sb_bubble
    ```
    
- 단계구분도 그리기
    - 시군구당 매장 수
        
        ```python
        sb_choropleth = folium.Map(location = [37.573050, 126.979189],
                              tiles = 'CartoDB positron',
                              zoom_start = 11)
                                   
        folium.Choropleth(geo_data = seoul_sgg_geo,
                         data = seoul_sb_sgg_final,
                         columns = ['시군구명','매장수'], # 데이터 간 비교 기준 및 사용 값
                          key_on = 'properties.SIG_KOR_NM', # 데이터 비교 기준(시군구명)
                          fill_color = 'Blues', # matplotlib colormap
                          fill_opacity = 0.7,
                          line_opacity = 0.5).add_to(sb_choropleth)
                                   
        sb_choropleth
        ```
        
    
    - 시군구당 주민등록인구 수
        
        ```python
        seoul_sb_sgg_final['주민등록인구'] = seoul_sb_sgg_final['주민등록인구'].str.replace(',','').astype('int')
        
        sb_choropleth_pop = folium.Map(location = [37.573050, 126.979189],
                              tiles = 'CartoDB positron',
                              zoom_start = 11)
                                   
        folium.Choropleth(geo_data = seoul_sgg_geo,
                         data = seoul_sb_sgg_final,
                         columns = ['시군구명','주민등록인구'],
                          key_on = 'properties.SIG_KOR_NM',
                          fill_color = 'Blues', # matplotlib colormap
                          fill_opacity = 0.7,
                          line_opacity = 0.5).add_to(sb_choropleth_pop)
                                   
        sb_choropleth_pop
        ```
        
    - 시군구 당 종사자 수
        
        ```python
        seoul_sb_sgg_final['종사자수'] = seoul_sb_sgg_final['종사자수'].str.replace(',','').astype('int')
        
        sb_choropleth_emp = folium.Map(location = [37.573050, 126.979189],
                              tiles = 'CartoDB positron',
                              zoom_start = 11)
                                   
        folium.Choropleth(geo_data = seoul_sgg_geo,
                         data = seoul_sb_sgg_final,
                         columns = ['시군구명','종사자수'],
                          key_on = 'properties.SIG_KOR_NM',
                          fill_color = 'Blues', # matplotlib colormap
                          fill_opacity = 0.7,
                          line_opacity = 0.5).add_to(sb_choropleth_emp)
        sb_choropleth_emp
        ```
        
    - 시군구 당 사업체 수
        
        ```python
        seoul_sb_sgg_final['사업체수'] = seoul_sb_sgg_final['사업체수'].str.replace(',','').astype('int')
        
        sb_choropleth_biz = folium.Map(location = [37.573050, 126.979189],
                              tiles = 'CartoDB positron',
                              zoom_start = 11)
                                   
        folium.Choropleth(geo_data = seoul_sgg_geo,
                         data = seoul_sb_sgg_final,
                         columns = ['시군구명','사업체수'],
                          key_on = 'properties.SIG_KOR_NM',
                          fill_color = 'Blues', # matplotlib colormap
                          fill_opacity = 0.7,
                          line_opacity = 0.5).add_to(sb_choropleth_biz)
                                   
        sb_choropleth_biz
        ```
        
    
    - 인구 10000명 당 시군구 별 매장 수
        
        ```python
        seoul_sb_sgg_final['인구 만명당 매장수'] = seoul_sb_sgg_final['매장수']/seoul_sb_sgg_final['주민등록인구']*10000
        
        sb_choropleth_10000 = folium.Map(location = [37.573050, 126.979189],
                              tiles = 'CartoDB positron',
                              zoom_start = 11)
                                   
        folium.Choropleth(geo_data = seoul_sgg_geo,
                         data = seoul_sb_sgg_final,
                         columns = ['시군구명','인구 만명당 매장수'],
                          key_on = 'properties.SIG_KOR_NM',
                          fill_color = 'Blues', # matplotlib colormap
                          fill_opacity = 0.7,
                          line_opacity = 0.5).add_to(sb_choropleth_10000)
                                   
        sb_choropleth_10000
        ```
        
    - 결국 스타벅스 매장 수는 주민등록 인구수와 관련이 없다는 결과를 알 수 있음
    
- 종사자 수 10000명당 매장 수 그리기
    
    ```python
    seoul_sb_sgg_final['종사자_만명당_매장수'] = seoul_sb_sgg_final['매장수']/seoul_sb_sgg_final['종사자수']*10000
    
    sb_emp10000 = folium.Map(location = [37.573050, 126.979189],
                          tiles = 'CartoDB positron',
                          zoom_start = 11)
                               
    def style_function(feature):
        return {'opacity' : 0.7, # 선 투명도
                'weight' : 1, # 선 두께
                'color' : 'red', # 선 색상
               'fillOpacity' : 0.1, # 선으로 이루어진 내부 투명도 설정
               'dashArray' : '5,5',} # 점선의 간격 설정
    
    folium.GeoJson(seoul_sgg_geo,
                  style_function = style_function).add_to(sb_emp10000)
    
    top = seoul_sb_sgg_final['종사자_만명당_매장수'].quantile(0.9) # 상위 10퍼센트의 값만 따로 저장
    
    for idx in seoul_sb_sgg_final.index:
        lat = seoul_sb_sgg_final.loc[idx, '위도']
        lng = seoul_sb_sgg_final.loc[idx, '경도']
        names = seoul_sb_sgg_final.loc[idx, '시군구명']
        r = seoul_sb_sgg_final.loc[idx, '종사자_만명당_매장수']
        
        if r > top:
            fillColor = '#FF3300' # 색상 지정 시 헥사코드 사용 가능
        else:
            fillColor = '#CCFF33' 
        
        folium.CircleMarker(location = [lat,lng],
                          color = 'gray',
                          radius = r*8,
                          weight = 2, # 외곽선 두께
                          fill = True, # 내부 채우기
                          fill_color = fillColor, # 내부 색상
                          fill_opacity = 1, # 내부 색상 투명도
                          tooltip = '<b>'+names+'</b>').add_to(sb_emp10000)
        
    sb_emp10000
    ```