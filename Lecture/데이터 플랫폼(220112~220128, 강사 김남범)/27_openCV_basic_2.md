# 30. openCV_basic_2

- 라이브러리 및 모듈 호출
    
    ```jsx
    import numpy as np
    import cv2
    import sys
    ```
    
- alpha channel image 활용하기
    - 데이터 확인 및 마스크 생성
        
        ```python
        img1 = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)
        img2 = cv2.imread('./fig/imgbin_sunglasses_1.png', cv2.IMREAD_UNCHANGED)
        
        # print(img1.shape)
        # print(img2.shape) # 1개 층이 더 존재
        
        if img1 is None or img2 is None:
            print('image read failed')
            sys.exit()
        
        sg = img2[:,:,:3]
        mask = img2[:,:,-1]
            
        cv2.imshow('img1',img1)
        cv2.imshow('img2',img2)
        cv2.imshow('sg',sg)
        cv2.imshow('mask',mask)
        
        while True:
            if cv2.waitKey()==27:
                break
                
        cv2.destroyAllWindows()
        ```
        
    
    - 강아지 사진에 안경 합성하기(수업 내용)
        
        ```python
        img1 = cv2.imread('fig/puppy.bmp', cv2.IMREAD_COLOR)
        img2 = cv2.imread('fig/imgbin_sunglasses_1.png', cv2.IMREAD_UNCHANGED)
        
        img2 = cv2.resize(img2, (300, 150))
        
        if img1 is None or img2 is None:
            print('Image read failed!')
            sys.exit()
        
        mask = img2[:, :, -1]    # mask는 알파 채널로 만든 마스크 영상
        glass = img2[:, :, 0:3]  # glass는 b, g, r 3채널로 구성된 컬러 영상
        
        h, w = mask.shape[:2]
        crop = img1[120:120+h, 220:220+w]  # glass mask와 같은 크기의 부분 영상 추출
        
        cv2.copyTo(glass, mask, crop)
        # crop[mask > 0] = (0, 0, 255) 하면 안경 빨간색으로 바뀜
        
        cv2.imshow('img1', img1)
        cv2.imshow('glass', glass)
        cv2.imshow('mask', mask)
        cv2.imshow('crop', crop)
        
        # cv2.imwrite('puppy_sunglass.bmp', src)
        
        cv2.waitKey()
        cv2.destroyAllWindows()
        ```
        
    - 강아지 사진에 안경 합성하기(내가 한 것)
        
        ```python
        img1 = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)
        img2 = cv2.imread('./fig/imgbin_sunglasses_1.png', cv2.IMREAD_UNCHANGED)
        h,w = img2.shape[:2]
        src = np.full((w,h,3), (255,0,255), dtype=np.uint8)
        mask = img2[:,:,-1]
        
        if img1 is None or img2 is None:
            print('image read failed')
            sys.exit()
        
        dst = img1[150:250,250:500]
        src_re = cv2.resize(src, (dst.shape[1], dst.shape[0]))
        mask_re = cv2.resize(mask, (dst.shape[1], dst.shape[0]))
            
        cv2.copyTo(src_re, mask_re, dst)
        
        cv2.imshow('img1',img1)
        
        while True:
            if cv2.waitKey()==27:
                break
                
        cv2.destroyAllWindows()
        ```
        
- openCV를 활용해 다양한 도형 그리기
    - 기본적인 도형 그리기
        
        ```python
        img = np.full((600,1200,3), 255, np.uint8) # 바탕 이미지 생성
        
        # 선
        cv2.line(img, # 그릴 바탕 영상
                (100,50), # 그림의 시작점(영상좌표)
                (300,50), # 그림의 끝점(영상좌표)
                (0,0,255), # 색상
                4, # 선 두께, default=1
                cv2.LINE_AA # 선 타입
                )
        cv2.line(img, (300,50), (200,250), (0,0,255), 4, cv2.LINE_AA)
        cv2.line(img, (400,50), (400,250), (0,0,255), 4, cv2.LINE_AA)
        
        # 화살표
        cv2.arrowedLine(img, (300,50), (200,250), (0,0,255), 4, cv2.LINE_AA)
        
        # 사각형
        cv2.rectangle(img,
                     (120,300), # 좌측 상단점
                     (400,400), # 우측 하단점
                     (0,0,255),
                     4,
                     cv2.LINE_AA)
        cv2.rectangle(img,
                     (100,300,300,100), # 사각형의 위치정보 (x,y,w,h)
                     (0,0,255),
                     4,
                     cv2.LINE_AA)
        
        # 원
        cv2.circle(img, 
                   (600,300), # 중심점
                   100, # 반지름
                   (255,0,255), 
                   10, 
                   cv2.LINE_AA)
        
        # 타원
        cv2.ellipse(img,
                   (600,300), # 타원의 중심점
                   (50,100), # 축의 길이(x,y)
                   10, # 타원의 기울기(12시기준 오른쪽으로 10도)
                   0, # 시작 각도
                   360, # 마지막 각도
                   (0,255,255),
                   10,
                   cv2.LINE_AA)
        
        # 텍스트
        text = 'openCV version = '+cv2.__version__
        cv2.putText(img,
                   text,
                   (800,100),
                   cv2.FONT_HERSHEY_COMPLEX_SMALL, # 글꼴
                   0.8, # 글자 사이즈
                   (0,0,255),
                   1,
                   cv2.LINE_AA)
        
        cv2.imshow('canvas',img)
        
        cv2.waitKey()
        cv2.destroyAllWindows()
        ```
        
    
    - 직선으로 글자 그리기
        
        ```python
        img = np.full((600,1200,3), 255, np.uint8)
        
        cv2.circle(img, (300,200), 100, (0,0,0), 5, cv2.LINE_AA)
        cv2.line(img, (500,100), (500,300), (0,0,0), 5, cv2.LINE_AA)
        cv2.line(img, (250,400), (250,500), (0,0,0), 5, cv2.LINE_AA)
        cv2.line(img, (250,500), (500,500), (0,0,0), 5, cv2.LINE_AA)
        
        cv2.line(img, (800,100), (675,300), (0,0,0), 5, cv2.LINE_AA)
        cv2.line(img, (770,150), (925,300), (0,0,0), 5, cv2.LINE_AA)
        cv2.line(img, (1025,100), (1025,300), (0,0,0), 5, cv2.LINE_AA)
        cv2.line(img, (1025,200), (1100,200), (0,0,0), 5, cv2.LINE_AA)
        cv2.rectangle(img, (750,400), (1000,500), (0,0,0), 4, cv2.LINE_AA)
        
        cv2.imshow('canvas',img)
        
        cv2.waitKey()
        cv2.destroyAllWindows()
        ```
        
- 동영상 데이터 활용
    - 데이터 읽기
        
        ```python
        cap = cv2.VideoCapture(0) 
        # 웹 캠이 여러개 일경우 0 대신 다른 숫자를 입력해 사용할 캠 선택
        # 숫자 대신 파일 경로를 입력할 경우, 해당 동영상 파일이 읽어짐
        
        if not cap.isOpened():
            print('video capture failed')
            sys.exit()
            
        while True:
            
            ret, frame = cap.read()
            
            if not ret:
                print('videos read failed')
                break
            # 외곽선만 표시(인수로 쓰인 숫자는 THRESHOLD를 의미)
            edge = cv2.Canny(frame, 50, 150) 
        		
            
            cv2.imshow('video', frame)
            cv2.imshow('edge',edge)
            
            if cv2.waitKey(20)==27: # 시간(최소한 영상의 프레임이 들어오는 시간보다는 짧아야 영상이 부드러움) 안 주면 첫번째 프레임만 들어오고 무한 대기
                break
            
        cap.release()
        cv2.destroyAllWindows()
        ```
        
    - 데이터 저장
        
        ```python
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print('video capture failed')
            sys.exit()
        
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 파일 너비 지정
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 파일 높이 지정
        fps = int(cap.get(cv2.CAP_PROP_FPS)*0.5) # 초당 프레임 지정
        fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 압축 형식 지정   
        
        out = cv2.VideoWriter('output_class.avi', fourcc, fps, (w,h)) # 객체생성
        out_2 = cv2.VideoWriter('output_edge_class.avi', fourcc, fps, (w,h)) # 객체생성
        out_3 = cv2.VideoWriter('output_edge_inverse_class.avi', fourcc, fps, (w,h))
        
        while True:
            
            ret, frame = cap.read()
            
            if not ret:
                print('videos read failed')
                break
                
            ## 영상 편집 부분 ##################
            edge = cv2.Canny(frame, 50, 150)
            edge_1 = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) # 객체가 컬러속성이기때문에 바꿔줘야함
            edge_2 = edge_1.copy()
            edge_2 = 255-edge_1 # 흑, 백 바꾸기
            ####################################
            
            cv2.imshow('video', frame)
            cv2.imshow('edge_1',edge_1)
            cv2.imshow('edge_2',edge_2)
            
            out.write(frame) # 객체에 읽은 프레임 쓰기
            out_2.write(edge_1)
            out_3.write(edge_2)
            
            if cv2.waitKey(20)==27:
                break
            
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        ```