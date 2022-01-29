# 20. 영상처리_histogram modification

- histogram
    - 픽셀의 값에 따른 수를 표현
    - 전체 수를 각 픽셀 수로 나누어 확률로 표현하면 normalized histogram
    - grayscale은 1 가지, color은 3 가지(RGB)
    
- histogram modification
    - contrast와 brightness를 histogram을 기반으로 개선하는 것
    - histogram의 모양과 범위에 집중
    - 종류
        - histogram scaling(stretching,shrinking)
            - normalization이라고도 함
            - 히스토그램을 더 넒거나 좁은 범위로 비율을 맞춰 변경
                
                $O(x,y)=[{ S_{max}-S{min} \over I_{max}-I_{min} }][I(x,y)-I_{min}]+S_{min}$
                
        - histogram sliding
            - 히스토그램을 offset만큼 이동시킴
                
                $O(x,y)=I(x,y)+offset$
                
        - histogram equalization
            - 히스토그램을 균일분포(uniform distribution) 형태를 띄도록 바꾸는 것
            - CDF(cumulative distribution function, 누적분포함수)가 우상향하는 직선을 그리도록 하는 것
                
                $O_{x,y}=E(I_{x,y},I)=[{ N_{max}-N_{min} \over T }][\sum_{l=0}^p I(l)]$
                
            - 알고리즘
                - 입력 영상의 히스토그램의 값을 누적시켜 각 레벨에서의 히스토그램 누적 합 계산
                - 히스토그램의 누적 합을 전체 픽셀의 개수로 나누어 값을 정규화
                - 정규화된 값에 대해 최대 gray level 값을 곱한 후 반올림
                - 입력 영상의 각 gray level에 대해 변환 값으로 대응
                
    - 단점
        - 배경 노이즈가 증가할 수 있음
        - near-constant region의 영상 퀄리티가 낮아질 수 있음