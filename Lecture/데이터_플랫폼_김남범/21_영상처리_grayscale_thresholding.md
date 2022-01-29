# 21. 영상처리_grayscale thresholding

- gray-level thresholding
    - threshold 값을 기준으로 낮으면 0, 높으면 최대값을 부여(binarization, 이진화)
    
- optimal threshold by OTSU
    - 기본 원리
        - 임계값 T를 기준으로 영역을 2개 그룹으로 나누었을 때, 집합 내의 명암 분포는 균일하고 집합 사이의 명암 차이는 최대화될 수 있도록 함
        - 모든 가능한 T에 대해 점수를 계산하여 가장 좋은 T를 최종 임계값으로 선택 → 최적화 알고리즘(optimization algorithm)
            - 낱낱 탐색(exhaustive search), 언덕 오르기(hill climbing) 등의 탐색 방법을 사용 가능
        - 최적화 알고리즘 에서는 비용함수(cost function) 또는 목적함수(objective function)을 사용하여 점수 계산
    
    - 목적함수
        - $T_{opt}=argmin_{1 \le k \le L-1}(\sigma^2(k))$
            - 두개의 그룹의 분산 합이 최소가 되는 k를 찾음
        - $\sigma^2_w(k)=\omega_1(k)\sigma^2_1(k)+\omega_2(k)\sigma^2_2(k)$
            - 분산 합, 즉 각 그룹간의 분산에 `개수/전체개수`를 곱해주는 것