# 28. openCV_intro

- 라이브러리 및 모듈 호출
  
    ```python
    import numpy as np
    import sys
    import cv2
    import os
    import matplotlib.pyplot as plt
    ```
    
- 이미지 파일 읽기 및 출력
  
    ```python
    img = cv2.imread('./fig/puppy.bmp')
    print(type(img)) # 읽은 파일은 np.ndarray 타입
    
    if img is None:
    	print('image read failed')
    	sys.exit()  # 예외 처리, 읽어올 파일이 없을 경우 종료
    
    cv2.namedWindow('image') # 이미지 창 이름 설정
    cv2.imshow('image',img) # 이미지 출력
    cv2.waitKey() # 아무 키나 입력하기 전까지 대기
    cv2.destroyAllWindows() # 모든 창 닫기
    ```
    
- 파일 읽을 때, 이미지 흑백/컬러 설정 및 사이즈 설정
  
    ```python
    # img = cv2.imread('파일경로', flags)
    # flags에 따라 설정 가능
    # cv2.IMREAD_COLOR는 컬러로(default)
    # cv2.IMREAD_GRAYSCALE는 흑백으로
    # cv2.IMREAD_REDUCED_COLOR_4는 컬러, 1/4 사이즈로
    # cv2.IMREAD_REDUCED_GRAYSCALE_8는 흑백, 1/8 사이즈로
    # cv2.IMREAD_UNCHANGED는 alpha channel(포토샵에서 투명 레이어 표시같은)까지 파일 속성 그대로
    
    img = cv2.imread('./fig/puppy_1280_853.jpg', cv2.IMREAD_REDUCED_GRAYSCALE_2)
    img_2 = cv2.imread('./fig/puppy_1280_853.jpg', cv2.IMREAD_COLOR)
    
    print(img.shape)
    print(img_2.shape)
    
    # 흑백의 경우, 2차원 array(행,열)
    # 컬러의 경우, 3차원 array(행,열,층)
    ```
    
- 파일을 읽은 후, 사이즈 변경 및 파일 저장하기
  
    ```python
    img = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)
    
    if img is None:
      print('image read failed')
      sys.exit()
    
    img_re = cv2.resize(img, # 소스 영상
                       (240,320), # 바꿀 사이즈
                       interpolation = cv2.INTER_AREA) # 보간법 지정
    img_re_2 = cv2.resize(img, 
                       (320,240), 
                       interpolation = cv2.INTER_AREA)
    
    cv2.namedWindow('image')
    cv2.namedWindow('image_re')
    cv2.namedWindow('image_re_2')
    cv2.imshow('image',img)
    cv2.imshow('image_re',img_re)
    cv2.imshow('image_re_2',img_re_2)
    
    # 파일 저장하기
    cv2.imwrite('./fig/puppy_resize.png', # 저장할 파일경로
                img_re_2) # 저장할 파일(np.array타입 데이터)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    # img는 (480, 640, 3)의 형태
    # img_re_2가 원하는 결과(절반으로 사이즈 줄이기)
    # opencv는 영상 좌표, 반환된 결과는 numpy array이므로 행렬 좌표를 쓰기 때문
    ```
    
- 이미지 창 설정
  
    ```python
    img = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)
    
    if img is None:
      print('image read failed')
      sys.exit()
    
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE) # 이미지 창 조절 불가능(default)
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 이미지 창 조절 가능
    cv2.moveWindow('image', 0, 0) # 이미지 창 위치 조절 (0,0 = 영상 좌표 x,y)
    cv2.imshow('image',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    ```
    
- waitKey()
  
    ```python
    # cv2.waitKey(시간(ms)) 
    # 키 입력이 되기 전까지 대기하는 용도
    # cv2.waitKey(3000)는 3000ms만큼만 대기
    # waitKey()는 입력 키에 해당하는 ASCII 코드 값을 반환
    # 아무 입력을 주지 않으면 -1을 반환
    
    cv2.destroyAllWindows()
    
    img = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)
    
    if img is None:
      print('image read failed')
      sys.exit()
        
    cv2.namedWindow('image')
    cv2.imshow('image',img)
    
    while True:                  # 'esc'를 입력했을 때만, 이미지창 닫기
      if cv2.waitKey() == 27:   # 27은 ESC의 ASCII code
        break
            
    # while True:                  # 'q'를 입력했을 때만, 이미지창 닫기
    #  if cv2.waitKey() == ord('q'):   # ord()를사용해 ASCII 코드 참조안하고 입력 가능
    #    break       
            
    cv2.destroyAllWindows()
    ```
    
- matplotlib을 활용해 이미지 출력하기
  
    ```python
    img = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)
    
    if img is None:
      print('image read failed')
      sys.exit()
        
    cv2.namedWindow('image')
    cv2.imshow('image',img)
    
    plt.imshow(img) 
    plt.axis('off')
    plt.show()
    
    while True:
      if cv2.waitKey() == 27:
        break
            
    cv2.destroyAllWindows()
    
    # opencv는 데이터를 BGR 순서로 읽어들이지만,
    # plt에서 BGR 데이터를 그대로 RGB 순으로 인식해서 색상이 이상함
    
    ```
    
    - 색상 정상적으로 출력하기 : cv2.cvtColor()
      
        ```python
        img = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)
        
        if img is None:
          print('image read failed')
          sys.exit()
            
        cv2.namedWindow('image') 
        cv2.imshow('image',img)
        
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 데이터를 RGB 순으로 변경
        plt.imshow(img_RGB)
        # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 데이터를 흑백으로 변경
        # plt.imshow(img_gray, cmap='gray') # cmap parameter 입력필수
        plt.axis('off')
        plt.show()
        
        while True:
        	if cv2.waitKey() == 27:
        	  break
                
        cv2.destroyAllWindows()
        ```
        
    - 여러 이미지 한 번에 출력하기
      
        ```python
        img = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)
        
        if img is None:
        	print('image read failed')
          sys.exit()
            
        cv2.namedWindow('image')
        cv2.imshow('image',img)
        
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 데이터를 RGB 순으로 변경
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 데이터를 흑백으로 변경
        
        plt.figure(figsize=(8,5))
        plt.subplot(131),plt.imshow(img),plt.axis('off')
        plt.subplot(132),plt.imshow(img_RGB),plt.axis('off')
        plt.subplot(133),plt.imshow(img_gray, cmap='gray'),plt.axis('off')
        plt.show()
        
        while True:
        	if cv2.waitKey() == 27:
            break
                
        cv2.destroyAllWindows()
        ```
    
- 슬라이드 쇼(디렉토리 내 이미지 순서대로 출력)
  
    ```python
    img_list = os.listdir('./fig/images/') # 특정 디렉토리 내 파일들의 이름을 리스트로
    
    img_path_list = []
    for img in img_list:
    	img_path = './fig/images/' + img
      img_path_list.append(img_path) # 파일 경로로 리스트 만들기
    
    cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 이미지 창 조절 가능
    cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) # 전체화면으로 출력
    
    for i in img_path_list:
      img = cv2.imread(i, cv2.IMREAD_COLOR)
    
    	if img is None:
    	  print('image read failed')
        sys.exit()
     
    	cv2.imshow('image',img)
      cv2.waitKey(2000)
    
    cv2.destroyAllWindows()
    
    ```
    
    - 디렉토리 내 이미지를 반복해서 출력하기(기존 슬라이드 쇼 무한 반복)
      
        ```python
        img_list = os.listdir('./fig/images/') # 특정 디렉토리 내 파일들의 이름을 리스트로
        
        img_path_list = []
        for img in img_list:
        	img_path = './fig/images/' + img
          img_path_list.append(img_path) # 파일 경로로 리스트 만들기
        
        i = 0
        while True:
          img = cv2.imread(img_path_list[i], cv2.IMREAD_REDUCED_COLOR_4) # 사이즈 조절
          cv2.imshow('image',img)
          if cv2.waitKey(2000) == 27: # 종료 조건
            break
          i += 1
          if i >= len(img_path_list):
            i = 0
        cv2.destroyAllWindows()
        ```
        
    - 특정 디렉토리 내 파일 리스트로 만들기
      
        ```python
        img_list = os.listdir('./fig/images/') # 특정 디렉토리 내 파일들의 이름을 리스트로
        
        img_path_list = []
        for img in img_list:
        	img_path = './fig/images/' + img
          img_path_list.append(img_path) # 파일 경로로 리스트 만들기
        
        # 위 과정은 상당히 길다.
        # glob 모듈을 사용하면 편하다.
        
        import glob
        
        img_path_list = glob.glob('./fig/images/*.jpg') # 해당 경로 내 jpg 확장자 파일을 모두 모아 리스트로 만듬
        
        ```