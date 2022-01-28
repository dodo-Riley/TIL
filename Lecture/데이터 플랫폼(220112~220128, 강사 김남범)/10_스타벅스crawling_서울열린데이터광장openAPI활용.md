# 10. 스타벅스 crawling_서울열린데이터 광장 open API 활용

> 교재에서는 open API를 활용해 필요 데이터를 수집했으나, 현재 서비스 종료로 인해 동일 과정 진행이 불가능. 따라서 open API를 활용하는 방법에 대해서만 정리
> 

- 서울열린데이터광장 오픈 API 활용하기
    
    ```python
    import requests
    # url형식은 아래와 같다.
    # url = 'http://openapi.seoul.go.kr:8088/{인증키}/{요청 파일 타입}/{서비스명}/{시작 위치}/{종료 위치}/'
    KEY = '****************************'
    service = 'GangseoListLoanCompany'
    
    url = f'http://openapi.seoul.go.kr:8088/{KEY}/json/{service}/1/5/'
    
    result_dict = requests.get(url).json()
    result_dict
    
    # 각 데이터에 접근하는 것은 파이썬 딕셔너리와 동일, ['key']를 통해 접근 가능
    sample_df = pd.DataFrame(result_dict['GangseoListLoanCompany']['row'])
    
    # 좌표계 WGS1984를 받아야 위/경도 데이터를 배운데로 사용할 수 있음
    ```
    
- 위 과정을 수행하는 함수 정의
    
    ```python
    KEY = '***************************'
    
    def seoul_open_api_data(url, service): # url과 서비스명을 인수로 받음
        data_list = None # 초기값 설정
        try:
            resilt_dict = requests.get(url).json() # 해당 데이터를 json 형식으로 추출
            result_data = result_dict[service] # 해당 서비스명의 데이터 추출
            code = result_data['RESULT']['CODE'] # 서비스명의 내의 코드 추출
            if code == 'INFO-000': # 코드가 성공적으로 추출한 수행의 코드라면
                data_list = result_data['row'] # 리스트에 row 키의 value를 저장
        except: # 데이터가 없다면 패스
            pass
        return data_list # 데이터 리스트 반환
    ```