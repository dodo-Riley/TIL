# 32. image processing_1

- 라이브러리 및 모듈 호출
    
    ```python
    import numpy as np
    import cv2
    import sys
    import matplotlib.pyplot as plt
    ```
    
- clipping
    
    ```python
    # grayscale 영상
    src = cv2.imread('./fig/lenna.bmp', cv2.IMREAD_GRAYSCALE)
    
    if src is None:
        print('image read failed')
        sys.exit()
    
    dst = np.clip(src + 100.0, # 실수형으로 입력해야함
                  0, # 최소 기준
                  255).astype(np.uint8) # 최대 기준, 다시 정수로 변환    
    
    # dst = cv2.add(src, 100) # 위와 같은 결과
    
    cv2.imshow('src',src)
    cv2.imshow('dst',dst)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    # color 영상
    src = cv2.imread('./fig/lenna.bmp', cv2.IMREAD_COLOR)
    
    if src is None:
        print('image read failed')
        sys.exit()
    
    dst = cv2.add(src, (100,100,100,0)) 
    # color의 경우 BGR,alpha까지 전부 값을 줘야함, 실제로는 이렇게 하지않고 HSV로 변환수 진행/재변환
    
    cv2.imshow('src',src)
    cv2.imshow('dst',dst)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    ```
    
- 산술 연산
    
    ```python
    src1 = cv2.imread('./fig/lenna256.bmp', cv2.IMREAD_GRAYSCALE)
    src2 = np.zeros_like(src1, np.uint8) # 특정 이미지와 같은 크기로 만들기
    cv2.circle(src2,(128,128),100,200,-1,cv2.LINE_AA)
    cv2.circle(src2,(128,128),50,50,-1,cv2.LINE_AA)
    
    dst1 = cv2.add(src1,src2) # 덧셈, clipping 자동
    dst2 = cv2.addWeighted(src1,0.5, src2, 0.5, 0.0) # 가중치를 더해서 합, ax+by+c 형태, 실수형 필수
    dst3 = cv2.subtract(src1,src2) # 앞에서 뒤를 뺄셈, 인자 순서에 따라 다른결과
    dst4 = cv2.absdiff(src1,src2) # 뺄셈의 절대값, 인자 순서 달라도 동일 결과
    
    plt.figure(figsize=(12,6))
    plt.subplot(231), plt.imshow(src1, cmap='gray'), plt.axis('off'), plt.title('src1')
    plt.subplot(232), plt.imshow(src2, cmap='gray'), plt.axis('off'), plt.title('src2')
    plt.subplot(233), plt.imshow(dst1, cmap='gray'), plt.axis('off'), plt.title('add')
    plt.subplot(234), plt.imshow(dst2, cmap='gray'), plt.axis('off'), plt.title('addweighted')
    plt.subplot(235), plt.imshow(dst3, cmap='gray'), plt.axis('off'), plt.title('sub')
    plt.subplot(236), plt.imshow(dst4, cmap='gray'), plt.axis('off'), plt.title('absdiff')
    plt.show()
    
    ```
    
- 비트 간 논리 연산
    
    ```python
    src1 = np.zeros((256,256), np.uint8)
    cv2.rectangle(src1, (10,10), (127,248), 255, -1)
    src2 = np.zeros((256,256), np.uint8)
    cv2.circle(src2, (128,128), 100, 255, -1)
    
    dst_bit_and = cv2.bitwise_and(src1,src2) # 둘 다 255일떄만 255
    dst_bit_or = cv2.bitwise_or(src1,src2) # 둘 다 0일때만 0
    dst_bit_xor = cv2.bitwise_xor(src1,src2) # 같으면 0, 다르면 255
    dst_bit_not = cv2.bitwise_not(src2) # 데이터를 반대로 바꿈
    
    plt.figure(figsize=(12,6))
    plt.subplot(231), plt.imshow(src1, cmap='gray'), plt.axis('off'), plt.title('src1')
    plt.subplot(232), plt.imshow(src2, cmap='gray'), plt.axis('off'), plt.title('src2')
    plt.subplot(233), plt.imshow(dst_bit_and, cmap='gray'), plt.axis('off'), plt.title('dst_bit_and')
    plt.subplot(234), plt.imshow(dst_bit_or, cmap='gray'), plt.axis('off'), plt.title('dst_bit_or')
    plt.subplot(235), plt.imshow(dst_bit_xor, cmap='gray'), plt.axis('off'), plt.title('dst_bit_xor')
    plt.subplot(236), plt.imshow(dst_bit_not, cmap='gray'), plt.axis('off'), plt.title('dst_bit_not')
    plt.show()
    ```
    
- color 영상을 BGR 각 층으로 나누고 합치기
    
    ```python
    src = cv2.imread('./fig/flowers.jpg')
    
    cv2.imshow('src',src)
    
    b,g,r = cv2.split(src) # B,G,R 순서로 데이터 나누기
    dst = cv2.merge([b,g,r]) # BGR로 데이터 합치기
    dst1 = cv2.merge([r,g,b]) # RGB 순서로 합치기
    dst2 = cv2.cvtColor(dst1, cv2.COLOR_RGB2BGR)
    
    cv2.imshow('b',b)
    cv2.imshow('g',g)
    cv2.imshow('r',r)
    cv2.imshow('dst',dst)
    cv2.imshow('dst1',dst1)
    cv2.imshow('dst2',dst2)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    ```