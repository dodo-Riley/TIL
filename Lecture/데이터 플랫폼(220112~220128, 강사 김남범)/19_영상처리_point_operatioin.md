# 19. 영상처리_point operatioin

- point operation
    - 특정 픽셀 값을 input해서 연산을 거친 후 output으로 얻어내는 것
    - techniques
        - arithmetic operation
        - grayscale transformation
        - histogram modification
    - 목표
        - improve contrast(대비) : 각 픽셀에 특정 값을 곱함
        - improve brightness(밝기) : 각 픽셀에 특정 값을 더하거나 곱함

- contrast & brightness
    - 히스토그램은 x축=intensity, y축=frequency
    - 히스토그램의 폭이 좁으면 contrast가 낮음
    - 히스토그램의 구간이 높은수록 brightness가 높음
    
- arithmetic operation
    - scalar arithmetic operation
        - $O(x,y)=k*I(x,y)+l(k=gain,l=level)$
        - clipping 처리 : output이 255보다 커지면 255로, 0보다 작아지면 0으로 처리
    - image arithmetic operation
        - 하드웨어적인 문제로 생기던 salt & pepper noise를 여러 이미지 픽셀 간의 평균으로 해결
        - 픽셀간 뺄셈을 통해 영상의 동일 유무인지 확인
- grayscale transformations
- processing for color images