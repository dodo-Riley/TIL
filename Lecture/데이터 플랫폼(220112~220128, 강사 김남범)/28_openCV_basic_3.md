# 31. openCV_basic_3

- 라이브러리 및 모듈 호출
    
    ```python
    import numpy as np
    import cv2
    import sys
    ```
    
- 키보드 이벤트 처리
    
    ```python
    img = cv2.imread('./fig/puppy.bmp', 0)
    
    if img is None:
        print('image read failed')
        sys.exit()
    
    img_c = img.copy() # 사본 생성
    
    cv2.imshow('image',img)
    
    while True:
        key = cv2.waitKey()
        
        if key==27: # esc 키 입력 시 루프 탈출
            break
            
        elif key==ord('e'):  # e 입력 시 edge 영상 출력
            img = cv2.Canny(img, 50, 150)
            cv2.imshow('image',img)
            
        elif key==ord('i'):  # i 입력 시 반전 영상 출력
            img = 255-img
            cv2.imshow('image',img)
        
        elif key==ord('r'): # r 입력 시 원본과 같은 사본 영상 출력
            img = img_c
            cv2.imshow('image',img)
            
    cv2.destroyAllWindows()
    ```
    
- 마우스 이벤트 처리
    - 콜백(callback) 함수
        - 매개 변수를 통해 다른 함수를 전달 받고, 이벤트가 발생할 때 매개 변수에 전달된 함수를 호출
        - 즉, 특정한 이벤트가 발생하면 다른 함수를 실행하는 함수
    
    - 마우스 콜백 함수의 매개 변수
        - event : 창에서 발생하는 이벤트
            
            
            | 이름 | 의미 |
            | --- | --- |
            | EVENT_MOUSEMOVE | 마우스 포인터가 윈도우 위에서 움직일 때 |
            | EVENT_LBUTTONDOWN | 마우스 왼쪽 버튼을 누를 때 |
            | EVENT_MBUTTONDOWN | 마우스 가운데 버튼을 누를 때 |
            | EVENT_RBUTTONDOWN | 마우스 오른쪽 버튼을 누를 때 |
            | EVENT_LBUTTONUP | 마우스 왼쪽 버튼을 뗄 때 |
            | EVENT_MBUTTONUP | 마우스 가운데 버튼을 뗄 때 |
            | EVENT_RBUTTONUP | 마우스 오른쪽 버튼을 뗄 때 |
            | EVENT_LBUTTONDBLCLK | 마우스 왼쪽 버튼을 더블 클릭할 때 |
            | EVENT_MBUTTONDBLCLK | 마우스 가운데 버튼을 더블 클릭할 때 |
            | EVENT_RBUTTONDBLCLK | 마우스 오른쪽 버튼을 더블 클릭할 때 |
            | EVENT_MOUSEWHEEL | 마우스 상하 스크롤을 사용할 때 |
            | EVENT_MOUSEHWHEEL | 마우스 좌우 스크롤을 사용할 때 |
        - x, y : 마우스의 좌표
        - flags : event와 함께 활용되며 특수한 상태를 확인하는 용도
            
            
            | 이름 | 의미 |
            | --- | --- |
            | EVENT_FLAG_LBUTTON | 마우스 왼쪽 버튼이 눌러져 있음 |
            | EVENT_FLAG_MBUTTON | 마우스 가운데 버튼이 눌러져 있음 |
            | EVENT_FLAG_RBUTTON | 마우스 오른쪽 버튼이 눌러져 있음 |
            | EVENT_FLAG_CTRLKEY | 컨트롤(Ctrl) 키가 눌러져 있음 |
            | EVENT_FLAG_SHIFTKEY | 쉬프트(Shift) 키가 눌러져 있음 |
            | EVENT_FLAG_ALTKEY | 알트(Alt) 키가 눌러져 있음 |
            | flags > 0 | 마우스 스크롤 이벤트의 윗 방향 또는 오른쪽 방향 |
            | flags < 0 | 마우스 스크롤 이벤트의 아랫 방향 또는 왼쪽 방향 |
        - param : 마우스 콜백 설정 함수에서 함께 전달되는 사용자 정의 데이터
        
    - 마우스 이벤트 처리 예시
        
        ```python
        img = np.ones((480,640,3), np.uint8)*255
        
        # 콜백 함수
        def call_mouse(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                print('left btn down = ', x,y)
            elif event == cv2.EVENT_LBUTTONUP:
                print('left btn up = ',x,y)
            elif event == cv2.EVENT_MOUSEMOVE:
                if flags ==cv2.EVENT_FLAG_LBUTTON:
                    print(x,y)
                
                
        cv2.imshow('image',img)
        
        # 마우스 콜백 설정 함수(항상 창을 띄우고 호출)
        cv2.setMouseCallback('image', # 창 이름
                             call_mouse, # 콜백 함수(마우스 이벤트가 발생했을 때 호출할 함수)
                             img) # 사용자 정의 데이터
        
        cv2.waitKey()
        cv2.destroyAllWindows()
        ```
        
    - 마우스로 글자 그리기(내가 한 것)
        
        ```python
        img = np.ones((480,640,3), np.uint8)*255
        a,b=0,0
        
        def call_mouse(event, x, y, flags, param):
            global a,b # 함수 밖의 변수 a,b를 함수 내에서도 사용
            
            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img, (x,y), 1, (255,0,255), -1, cv2.LINE_AA)
                a,b=x,y
                cv2.imshow('image',img)
                
            elif event == cv2.EVENT_MOUSEMOVE:
                if flags ==cv2.EVENT_FLAG_LBUTTON:
                    cv2.line(img, (a,b), (x,y), (255,0,255), 2, cv2.LINE_AA)
                    a,b=x,y
                    cv2.imshow('image',img)
                
        cv2.imshow('image',img)
        
        cv2.setMouseCallback('image', call_mouse, img)
        
        while True:
            key = cv2.waitKey()
            
            if key==27:
                break
                
            elif key==ord('s'):
                cv2.imwrite('./fig/letters.bmp', img) # s누르면 저장
        
        cv2.destroyAllWindows()
        ```
        
    
    - 마우스로 글자 그리기(수업내용)
        
        ```python
        oldx = oldy = 0
        
        def call_mouse(event, x, y, flags, param):
            global oldx, oldy
        
            if event == cv2.EVENT_LBUTTONDOWN:
                oldx, oldy = x, y
                print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
        
            elif event == cv2.EVENT_LBUTTONUP:
                print('EVENT_LBUTTONUP: %d, %d' % (x, y))
        
            elif event == cv2.EVENT_MOUSEMOVE:
                if flags & cv2.EVENT_FLAG_LBUTTON:
                    cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
                    cv2.imshow('image', img)
                    oldx, oldy = x, y
        
        img = np.ones((480, 640, 3), dtype=np.uint8) * 255
        
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', call_mouse, img) 
        
        cv2.imshow('image', img)
        
        while True:
            key = cv2.waitKey()
            
            if key==27:
                break
                
            elif key==ord('s'):
                cv2.imwrite('./fig/letters.bmp', img) # s누르면 저장
        
        cv2.destroyAllWindows()
        ```
        
    
- 트랙바
    - 트랙바 사용하기
        
        ```python
        img = np.zeros((480,640), np.uint8)
        
        def call_trackbar(pos):
            img[:]=pos
            cv2.imshow('image',img)
        
        cv2.namedWindow('image')
        cv2.createTrackbar('level', # 트랙바 이름
                          'image', # 창 이름
                          50, # 트랙바 시작값
                          255, # 트랙바 최대값
                          call_trackbar) # 콜백함수
        
        cv2.imshow('image', img)
        
        cv2.waitKey()
        cv2.destroyAllWindows()
        ```
        
    
    - 알파 채널 영상에 트랙바 활용
        
        ```python
        img = cv2.imread('./fig/imgbin_sunglasses_1.png', cv2.IMREAD_UNCHANGED)
        mask = img[:,:,-1] # 알파 채널 데이터만 가져오기
        mask[mask>0]=1 # 데이터를 0과 1로 만들기 
        
        def call_trackbar(pos):
            global mask
            img_glass=mask*pos
            cv2.imshow('image',img_glass)
            
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.createTrackbar('level', 'image', 0, 255, call_trackbar)
        cv2.imshow('image',img) # 트랙바의 값에 따라 영상 출력이 달라짐
        
        cv2.waitKey()
        cv2.destroyAllWindows()
        ```
        

> 참고 : [https://076923.github.io/posts/Python-opencv-39/](https://076923.github.io/posts/Python-opencv-39/)
>