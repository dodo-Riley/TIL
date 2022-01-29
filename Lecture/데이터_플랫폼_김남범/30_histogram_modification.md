# 30. histogram modification

- 라이브러리 및 모듈 호출
    
    ```python
    import sys
    import numpy as np
    import matplotlib.pyplot as plt
    import cv2
    ```
    
- 영상의 히스토그램 그리기
    
    ```python
    src_gray = cv2.imread('./fig/lenna.bmp', cv2.IMREAD_GRAYSCALE)
    src_c = cv2.imread('./fig/lenna.bmp', cv2.IMREAD_COLOR)
    
    if src_g is None:
        sys.exit('image read failed')
    
    hist_gray = cv2.calcHist([src_gray], # 입력영상(리스트로 넣어야함)
                       [0], # 채널리스트(컬러와 같이 3채널일경우, [0,1,2])
                       None, # 마스크 영상(영상 일부만 사용하려고 할때 해당 마스크 입력)
                       [256], # 히스토그램 구간 개수
                       [0,256] # 히스토그램의 최대값과 최소값
                       )
    
    # 컬러 영상의 경우, bgr별로 따로 그리기
    hist_b = cv2.calcHist([src_c], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([src_c], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([src_c], [2], None, [256], [0, 256])
    
    cv2.imshow('src_gray', src_gray)
    cv2.imshow('src_c', src_c)
    
    plt.plot(hist_gray, color = 'k')
    plt.plot(hist_b, color = "b")
    plt.plot(hist_g, color = "g")
    plt.plot(hist_r, color = "r")
    plt.show()
    
    while True:
        key = cv2.waitKey()
        
        if key == 27:
            break
            
    cv2.destroyAllWindows()
    ```
    
- 히스토그램 정규화(normalizing)와 평활화(equalizing)
    - grayscale 영상
        
        ```python
        src = cv2.imread('./fig/Hawkes.jpg', 0)
        
        # 정규화
        dst_norm = cv2.normalize(src, # 입력 영상
                                None, # 결과 영상(defaut=none)
                                0, 255, # 정규화 최초값과 최대값
                                cv2.NORM_MINMAX,# 정규화 종류
                                -1 # 결과영상의 타입(-1이면 동일한 타입으로)
                                )
        # 평활화
        dst_equal = cv2.equalizeHist(src)
        
        cv2.imshow('src',src)
        cv2.imshow('dst_norm',dst_norm)
        cv2.imshow('dst_equal',dst_equal) # 어떤 방식이 더 나은지는 해봐야 안다
        
        cv2.waitKey()
        cv2.destroyAllWindows()
        ```
        
    - color 영상
        
        ```python
        src = cv2.imread('./fig/field.bmp')
        
        src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV) # BGR을 HSV로 변환
        h,s,v=cv2.split(src_hsv) # H,S,V 나누기
        v_equal = cv2.equalizeHist(v) # V(명도) 값만 평활화
        src_hsv_equal = cv2.merge([h,s,v_equal]) # 합치기
        src_bgr_equal = cv2.cvtColor(src_hsv_equal, cv2.COLOR_HSV2BGR) # 다시 BGR로 변환
        
        cv2.imshow('src',src)
        cv2.imshow('src_equal',src_bgr_equal)
        
        cv2.waitKey()
        cv2.destroyAllWindows()
        ```