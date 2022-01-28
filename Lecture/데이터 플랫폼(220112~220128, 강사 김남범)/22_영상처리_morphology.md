# 22. 영상처리_morphology

- morphology(형태학)
    - 생물학의 한 분야로 동물이나 식물의 모양이나 구조를 다루는 학문
    
- mathematical morphology(수학적 형태학)
    - 관심 객체의 검출을 쉽게 처리할 수 있도록 영상 분할 결과를 단순화하는 방법으로 사용
    - 객체 경계의 다순화, 작은 구멍을 채움, 작은 돌기의 제거 등
    - binary 영상과 grayscale 영상에 적용 가능
    - morphology filtering
        - 구조적 요소(structuring element)와 팽창(dilation) 및 침식(erosion) 연산 사용
        
- dilation operation(팽창 연산)
    - 객체의 크기를 확장
        - 객체 내부의 작은 구멍을 채움
        - 근접한 위치의 두 객체를 연결
    - 연결성
        - anchor point를 기준으로 몇 개의 structuring element가 연결되었는지에 따라 4연결성, 8연결성 등으로 구분
    - 알고리즘
        - 구조적 요소의 중심이 영상의 ‘0’에 위치하면 다음 위치로 이동
        - 구조적 요소의 중심이 영상의 ‘1’에 위치하면 구조 요소와 영상을 논리적 OR연산 수행(anchor point와 연결된 요소들을 채움)
        
- erosion operation(침식 연산)
    - 객체의 크기를 축소
        - 객체 경계를 침식
        - 작은 돌기를 제거
    - 알고리즘
        - 구조적 요소의 중심이 영상의 ‘0’에 위치하면 다음 위치로 이동
        - 구조적 요소의 중심이 영상의 ‘1’에 위치하면 구조 요소에서 ‘1’위치가 하나라도 객체를 벗어나면 그 위치는 ‘0’으로 변경(anchor point와 연결된 요소 중 하나라도 객체를 벗어나면 anchor point를 비움)
        
- opening operation(열림 연산)
    - 침식 연산을 수행한 후 다시 팽창 연산 적용
    - 작은 크기의 객체에 포함되는 픽셀들을 제거
    
- closing operation(닫힘 연산)
    - 팽창 연산을 수행한 후 다시 침식 연산 적용
    - 객체 내부의 작은 구멍이나 간격을 채움