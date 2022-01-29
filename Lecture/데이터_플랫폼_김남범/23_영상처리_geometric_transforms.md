# 23. 영상처리_geometric transforms

- geometric transforms

  - 수식이나 변환 관계에 의해 픽셀들의 위치를 변경하는 변환
  - 2 단계의 처리 단계로 구성
    - mapping by spatial transform
    - gray-level interpolation

- spatial transform

  - input 영상의 위치를 output 영상의 위치로 mapping

  - 종류

    - scaling(확대, 축소)
    - rotation(회전)
    - translation(이동)
    - skew(기울임, shear)

  - mapping 방식

    - forward mapping
      - 변환 수식에 의해 입력 좌표를 출력 좌표로 변환하는 과정
      - 출력 영상에서 정의되지 않은 픽셀 발생(hole)
    - backward mapping
      - 출력 영상의 각 픽셀 좌표에 대응하는 원본 연상의 좌표를 계산하여 해당 픽셀의 밝기 값을 결정하는 방법
      - 출력 영상에서 정의되지 않은 픽셀 발생 방지
      - 계산된 좌표가 정수가 아닌 경우 발생 → interpolation 적용

  - affine transform

    - linear transform

    - 휘어짐이 없고 평행한 선들은 평행을 유지하는 변환

    - 이동, 회전, 스케일링 및 이들의 조합에 의한 변환

    - $x'=a_0x+a_1y+a_2, y'=b_0x+b_1y+b_2$

    - homogeneous coordinate system(동차 좌표계) 사용

      $\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}= \begin{bmatrix} a_0 & a_1 & a_2 \\ b_0 & b_1 & b_2 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$

      - translation

        $\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}= \begin{bmatrix} 1 & 0 & T_x \\ 0 & 1 & T_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$(forward mapping)

        $\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}= \begin{bmatrix} 1 & 0 & -T_x \\ 0 & 1 & -T_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}$(backward mapping)

      - rotation

        $\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}= \begin{bmatrix} cos\theta & -sin\theta & 0 \\ sin\theta & cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$(forward mapping)

        $\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}= \begin{bmatrix} cos\theta & sin\theta & 0 \\ -sin\theta & cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}$(backward mapping)

      - scaling

        $\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}= \begin{bmatrix} S_x & 0 & 0 \\ 0 & S_y & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$(forward mapping)

        $\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}= \begin{bmatrix} S_x^{-1} & 0 & 0 \\ 0 & S_y^{-1} & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}$(backward mapping)

      - skew

        $\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}= \begin{bmatrix} 1 & u & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$(forward mapping)

        $\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}= \begin{bmatrix} 1 & -u & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}$(backward mapping)

- warping

  - nonlinear transform(rubber sheet transform)

  - 픽셀별로 이동 정도를 다르게 할 수 있어서 고무판 위에 그려진 영상을 임의대로 구부리는 것과 같은 효과를 낼 수 있음

  - 고차항을 사용하여 일반화된 다항식으로 표현

    $x'=\sum\limits_{i=0}^{N}\sum\limits_{j=0}^{N-i}a_{ij}x^iy^i,y'=\sum\limits_{i=0}^{N}\sum\limits_{j=0}^{N-i}b_{ij}x^iy^i$

- interpolation

  - 결과 픽셀에 정확하게 대응되는 입력 픽셀이 없는 경우, 주변 픽셀을 고려하여 새로운 값을 생성하는 방법
  - 종류
    - nearest neighbor interpolation
      - 계산한 위치에서 가장 가까운 원시 픽셀을 선택하는 방법
      - 처리 속도는 빠르지만 결과 영상의 질이 좋지 않음
    - neighbor averaging interpolation(
      - 주변 픽셀의 평균을 선택하는 방법
      - 2차원의 경우, 4개의 주변 픽셀 사용
      - 처리 속도는 조금 느려지지만 더 나은 결과 영상
    - bilinear interpolation
      - 새로운 픽셀을 생성하기 위해 네 개의 가장 가까운 픽셀들에 가중치를 곱한 값들의 합을 사용
      - 보다 자연스러운 영상을 산출
    - higher order interpolation