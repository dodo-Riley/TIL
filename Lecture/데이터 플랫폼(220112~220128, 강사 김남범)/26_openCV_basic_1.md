# 29. openCV_basic_1

- 라이브러리 및 모듈 호출
    
    ```python
    import numpy as np
    import cv2
    import sys
    ```
    
- 이미지 정보 확인하기
    
    ```python
    img = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_GRAYSCALE)
    img_c = cv2.imread('./fig/puppy_1280_853.jpg', cv2.IMREAD_COLOR)
    
    if img is None or img_c is None:
    	print('image read failed')
      sys.exit()
    
    print('img type = ', type(img), sep='')     
    print('img dimension = ', len(img.shape), sep='')
    print('img data type = ', img.dtype, sep='')
    h,w=img.shape[:2] # 컬러의 경우, (행,열,층)으로 나오기 때문에 [:2]를 해줘야함
    print(f'img size = {w} X {h}') # 영상 좌표와 행렬 위치는 서로 반대
    
    print('img_c type = ', type(img_c), sep='')
    print('img_c dimension = ', len(img_c.shape), sep='')
    print('img_c data type = ', img_c.dtype, sep='')
    h_c,w_c=img_c.shape[:2]
    print(f'img_c size = {w_c} X {h_c}')
    
    ```
    
- 픽셀값 참조 및 변경
    
    ```python
    img_1 = cv2.imread('./fig/puppy.bmp', 1) # cv2.IMREAD_COLOR와 동일
    img_2 = cv2.imread('./fig/puppy.bmp', 0) # cv2.IMREAD_GRAYSCALE과 동일
    
    if img_1 is None or img_2 is None:
        print('image read failed')
        sys.exit()
    
    # 가운데 픽셀 찾기
    h1,w1=img_1.shape[:2] # 전체 사이즈
    img_1_center = img_1[h1//2,w1//2] # 가운데 픽셀의 값
    print(img_1_center) # BGR 순서대로 3개 나옴
    
    h2,w2=img_2.shape[:2]
    img_2_center = img_2[h2//2,w2//2]
    print(img_2_center) # grayscale이므로 한개 나옴
        
    # 특정 픽셀의 값 찾기
    x,y=(120,320)
    p1 = img_1[y,x]
    p2 = img_2[y,x]
    print(p1, p2)
    
    # 특정 픽셀 값 변경
    img_1[10:110, 100:200] = 0
    img_1[10:110, 200:300] = (0,0,255) # BGR 순서
    img_1[10:110, 300:400] = (0,255,0)
    img_2[10:110, 100:200] = 255
    # img_2[10:110, 100:200] = (0,0,255) # 애초에 grayscale이기 때문에 불가능
    
    cv2.imshow('image_1',img_1)
    cv2.imshow('image_2',img_2) # 이미지에서 해당 픽셀들이 변경된 것 확인 가능
    cv2.waitKey()
    cv2.destroyAllWindows()
    ```
    
- 이미지 생성
    
    ```python
    img_c = np.zeros((240,320,3), dtype=np.uint8) # 검은 이미지 생성(color)
    img_g = np.ones((240,320), dtype=np.uint8)*255 # 밝은 이미지 생성(gray)
    img_c_w = np.full((240,320,3), 255, dtype=np.uint8) # 밝은 이미지 생성(color)
    img_random = np.random.randint(0,255, size=(240,320), dtype=np.uint8) # 불규칙한 이미지 생성(gray)
    
    img_c[10:60, 10:60] = (0,255,0)
    img_g[10:60, 10:60] = 0
    
    cv2.imshow('image_c',img_c)
    cv2.imshow('image_g',img_g)
    cv2.imshow('image_c_w',img_c_w)
    cv2.imshow('image_random',img_random)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    ```
    
- 영상 복사
    
    ```python
    img = cv2.imread('./fig/cat.bmp')
    
    if img is None:
        print('image read failed')
        sys.exit()
        
    img_1 = img # 같은 메모리 주소를 가리킴
    img_2 = img.copy() # 새로운 메모리 주소를 가리킴, 원본을 살리기위해서는 copy() 사용 필요
    
    img[100:200, 200:300] = (0,0,255)
    
    cv2.imshow('image',img)
    cv2.imshow('image_1',img_1) # img를 수정했지만 img1도 같이 바뀜
    cv2.imshow('image_2',img_2)
    
    while True:
        if cv2.waitKey() == 27:
            break
            
    cv2.destroyAllWindows()
    ```
    
- 원 그리기
    
    ```python
    img = np.ones((400,400,3), dtype=np.uint8)*255 # 바탕 이미지 생성
    
    if img is None:
        print('image read failed')
        sys.exit()
        
    img_1 = img.copy() # 이미지 복사
    
    cv2.circle(img_1, # 그릴 바탕 이미지
             (200,200), # 중심
              100, # 반지름
              (0,0,255), # 색상
              3, # 두께 (-1을 쓰면 내부채우기)
              cv2.LINE_AA # 선 타입 안티앨리어싱(부드럽게) (default = LINE_8)
              )
    cv2.imshow('image',img_1)
    cv2.waitKey()
    cv2.destroyAllWindows()
    ```
    
- 특정부분을 잘라 수정하기
    
    ```python
    img = cv2.imread('./fig/puppy.bmp',1)
    if img is None:
        print('image read failed')
        sys.exit()
    
    img_1 = img.copy() # img는 원본, img_1은 같은 파일이지만 작업을 진행할 파일
    h,w = img_1.shape[:2]
    img_2 = img_1[h//2-50:h//2+150,w//2-50:w//2+150] # 작업할 부분만 잘라내기
    img_3 = img_2.copy()
    
    cv2.circle(img_2, (140,100), 50, (0,0,255), 3, cv2.LINE_AA)
    
    cv2.imshow('image_1',img_1)
    cv2.imshow('image_2',img_2)
    cv2.imshow('image_3',img_3)
    
    while True:
        if cv2.waitKey() == 27:
            break
    cv2.destroyAllWindows()
    ```
    
- copyTo 사용하기
    
    ```python
    src = cv2.imread('./fig/airplane.bmp', 1)
    mask = cv2.imread('./fig/mask_plane.bmp', 0)
    dst = cv2.imread('./fig/field.bmp', 1)
    
    if src is None or mask is None or dst is None:
        print('image read failed')
        sys.exit()
    
    cv2.copyTo(src, # 소스 영상(뽑아낼 영상의 원본)
              mask, # 마스크 영상(뽑아낼 모양)
              dst) # destination 영상(바탕이 되는 영상) # dimension이 동일해야 제대로 동작
    
    cv2.imshow('src',src)
    cv2.imshow('mask',mask)
    cv2.imshow('dst',dst)
    
    while True:
        if cv2.waitKey() == 27:
            break
    cv2.destroyAllWindows()
    ```
    
- 마스크 이미지 생성하기
    
    ```python
    src = cv2.imread('./fig/airplane.bmp', 1)
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    ret, mask = cv2.threshold(src_gray, # 사용할 영상
                             160, # 문턱
                             255,# 최대값
                             cv2.THRESH_BINARY_INV) # 문턱아래는 1, 문턱부터 최대값까지는 0
    
    if src is None :
        print('image read failed')
        sys.exit()
    
    cv2.imshow('src',src)
    cv2.imshow('src_gray',src_gray)
    cv2.imshow('mask',mask)
    
    while True:
        if cv2.waitKey() == 27:
            break
    cv2.destroyAllWindows()
    
    # 복잡한 이미지(색상 차이가 약하거나, 구조가 복잡한 경우 등)는 추가적인 작업이 있어야 완전한 마스크를 얻을 수 있음
    ```
    
- 직접 해보기 : 초원위의 송아지 합성하기
    
    ```python
    src = cv2.imread('./fig/cow.png', 1)
    src_gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    dst = cv2.imread('./fig/green.png', 1)
    
    if src is None or dst is None :
        print('image read failed')
        sys.exit()
        
    ret, mask = cv2.threshold(src_gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    h,w = src.shape[:2]
    a,b = dst.shape[:2]
    dst_2 = dst[a//2-h//2+180:a//2+h//2+180,b//2-w//2:b//2+w//2]
    
    cv2.copyTo(src, mask, dst_2)
    
    cv2.imshow('src',src)
    cv2.imshow('mask',mask)
    cv2.imshow('dst',dst)
    
    while True:
        if cv2.waitKey() == 27:
            break
    cv2.destroyAllWindows()
    ```
    
- 직접 해보기 : 하늘에서 돈이 떨어진다.
    
    ```python
    src = cv2.imread('./fig/money.png')
    dst = cv2.imread('./fig/green.png', 1)
    
    if src is None or dst is None :
        print('image read failed')
        sys.exit()
    
    a,b = dst.shape[:2]
    
    src_2 = cv2.resize(src, (b//2,a//2), interpolation=cv2.INTER_AREA) # 사이즈가 안맞아 수정
    src_gray = cv2.cvtColor(src_2, cv2.COLOR_RGB2GRAY)
    
    ret, mask = cv2.threshold(src_gray, 200, 255, cv2.THRESH_BINARY_INV)
    
    h,w = src_2.shape[:2]
    
    dst_2 = dst[a//2-h//2-280:a//2+h//2-280,b//2-w//2-370:b//2+w//2-370]
    dst_3 = dst[a//2-h//2-280:a//2+h//2-280,b//2-w//2+370:b//2+w//2+370]
    cv2.copyTo(src_2, mask, dst_2)
    cv2.copyTo(src_2, mask, dst_3) # 같은 이미지를 다른 구간에 반복해서 적용
    
    cv2.namedWindow('dst', cv2.WINDOW_NORMAL) # 이미지 창 크기 조절 가능하도록
    
    cv2.imshow('src',src)
    cv2.imshow('mask',mask)
    cv2.imshow('dst',dst)
    
    while True:
        if cv2.waitKey() == 27:
            break
    cv2.destroyAllWindows()
    ```