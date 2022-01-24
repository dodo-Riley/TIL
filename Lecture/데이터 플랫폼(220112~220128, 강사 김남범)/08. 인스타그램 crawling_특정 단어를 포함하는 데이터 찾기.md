# 8. 인스타그램 crawling_특정 단어를 포함하는 데이터 찾기

> `6. 인스타그램 crawling_데이터 전처리`에서 처리한 데이터를 사용
> 

- 특정 단어가 들어간 데이터 찾아서 출력하기
    
    ```python
    import pandas as pd
    
    # 사용할 데이터 가져오기
    raw_total = pd.read_excel('./files/1_crawling_raw.xlsx')
    
    # 특정 단어가 들어간 내용 찾아서 출력하기
    select_word = '해돋이' # 찾을 단어
    check_list = [] # 단어가 해당 데이터에 존재하는 여부를 담을 리스트 초기화
    
    for content in raw_total['content']: # raw_data의 content 컬럼의 모든 행에 대해
        if select_word in content: # 특정 단어가 있으면
            check_list.append(True) # 참을 저장
        else:
            check_list.append(False) # 없으면 거짓을 저장
            
    select_df = raw_total[check_list] # 특정 단어가 있어서 참인 행만 저장
    
    for i in select_df.index: # select_df의 모든 인덱스에 대해
        print(select_df.loc[i, 'content'], end='\n'+'-'*50+'\n') # 해당 행의 content 컬럼의 값을 출력
    ```
    
- 혼자 해보기 : 위 과정을 함수로 정의하고 결과를 단순 리스트로 반환하기
    
    ```python
    def my_select_word(fpath, word):
    
        data_total_df = pd.read_excel(f'{fpath}') # 사용할 파일 불러오기
        check_list = [] 
        result = [] # 리스트 초기화
        
        for content in data_total_df['content']:
            if word in content:
                check_list.append(True)
            else:
                check_list.append(False)
                
        select_word_content = data_total_df[check_list]
        
        for i in select_word_content.index:
            data = select_word_content.loc[i, 'content']
            result.append(data)
            
        return result
    
    ### 메인부
    my_select_word('./files/1_crawling_raw.xlsx','해돋이')
    ```
    
- 여러 개의 단어 목록을 받아 처리하기
    
    ```python
    select_word_list = ['해돋이','박물관','힐링','게스트하우스','섭지코지']
    
    def select_word(select_word_list):
        for select_word in select_word_list: # 목록의 모든 단어들에 대해서
            check_list = []
            for content in raw_total['content']: # 개별 과정은 이전과 동일하게 반복
                if select_word in content:
                    check_list.append(True)
                else:
                    check_list.append(False)
                    
            select_df = raw_total[check_list]
            fpath = f'./files/4_select_data_{select_word}_class.xlsx'
            select_df.to_excel(fpath, index=False)
        
    select_word(select_word_list)
    ```
    
- 혼자 해보기 : 내가 만든 함수를 이용해 모든 데이터가 아닌 내용만 여러 단어들에 대해 저장하기
    
    ```python
    # 여러 군데의 서로 다른 파일에 대해서도 같은 작업을 반복할 수 있도록 함수 정의
    
    select_word_list = ['해돋이','박물관','힐링','게스트하우스','섭지코지']
    fpath_list = ['./files/1_crawling_raw.xlsx'] 
    
    def select_word(fpath, word):
        data_total_df = pd.read_excel(f'{fpath}')
        check_list = []
        result = []
        
        for content in data_total_df['content']:
            if word in content:
                check_list.append(True)
            else:
                check_list.append(False)
                
        select_word_content = data_total_df[check_list]
        
        for i in select_word_content.index:
            data = select_word_content.loc[i, 'content']
            result.append(data)
            
        return result
    
    for fpath in fpath_list:
        for word in select_word_list:
            result = pd.DataFrame(select_word(fpath,word))
            result.to_excel(f'./files/{word}_내용추출.xlsx', index=False)
    ```