# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 16:12:05 2021

@author: sjh73
"""

# 자료 구조
# 1. 리스트(list, 기본구조)   [1,2]
# 2. 튜플(tuple, 상수)     (1,2)
# 3. 딕셔너리(key:value)  << json {1:'양진욱',2:'백혜림',3:'박윤수'}
# 4. 세트(set, 집합) set()
# 5. 배열(numpy)
# 6. 판다스 구조(series, dataframe)

# numpy
# 배열(array) 생성, 연산

# 배열 : 하나의 데이터 타입 허용(int, float 등 ex)한 어레이 안에 문자와 정수가 같이 있을수 없음, 다차원 자료구조

import numpy as np
np.array([1,2,3])
# array([1, 2, 3]) 1차원 배열

np.array([[1,2,3],[4,5,6],[7,8,9]])
#  array([[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]) 2차원 배열 (수리적 모형 : 행렬)

np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],
   
#        [[ 7,  8,  9],
#         [10, 11, 12]]]) 3차원 배열

np.arange(1,26)
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
#         18, 19, 20, 21, 22, 23, 24, 25])  인자가 25개

np.arange(1,26).reshape(5,5)
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])

np.arange(1,26).reshape(5,-1) # > 인자가 많아서 끝이 몇인지 모른다? -1 넣으면 알아서 만들어줌

a1=np.arange(1,26)
type(a1)

# 색인 
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# array[행 선택, 열 선택]
a2[1,:]
# array([4, 5, 6])

a2[:,1]                # 정수 색인(두번째 열 선택 : 차원 축소 발생)
# array([2, 5, 8])

a2[:,1:2]              # 슬라이스 색인(두번째 열 선택 : 차원 축소 발생하지 않음)
# array([[2],
#       [5],
 #      [8]])

# a2에서 1,3행 선택하기
a2[[0,2],:]

a2
a2[1,1] # 5 return
a2[[1,2],[1,2]] # array([5,9])  >>원하는 대로 안나온 결과, 난 1,2행의 1,2열을 원했지만 5,9만 나온결과

#  >>> a2[1,1], a2[2,2] 포인트 인덱싱
#                            2개의 포인트(점) 출력
#                            색인함수(ix_()) 사용하여 해결

a2[np.ix_([1,2],[1,2])]
# array([[5, 6],
#        [8, 9]])  >>>>원하는 대로 나온 결과!

# 조건 색인
a2 > 5
# array([[False, False, False],
#       [False, False,  True],
#       [ True,  True,  True]])

a2[a2>5]
# array([6, 7, 8, 9]) > true만 출력됨

a2[:,0] > 5 # 첫 column 가져와서 5이상인 행만 선택

a2[0,0:2] > 5
a2[a2[0,:2] > 5]

a2[a2[:,0] > 5]  # 첫번째 컬럼이 5 이상인 행 색인 
a2[a2[:,0] > 5,:] # 위랑 같은 결과, 위에는 ,:가 생략된건가?
# array([[7, 8, 9]])
# 조건의 결과를 행방향에 색인 값으로 전달

# 3. 메소드
a2.shape()
dir(a2) # a2에 대해 쓸수 있는 거 보여줌

a2.dtype  # numpy 구성 데이터 타입
a2.shape  # numpy 모양(shape)
a2.shape[0]  #numpy 행의 수
a2.shape[1]   # numpy 열(column) 수

a2.reshape(1,9) # array 모양 변경
a2.ndim  #array 차원

# 4. 연산
[1,2,3] + [4,5,6]    # list는 서로 원소끼리 연산불가 (확장으로 해석됨)
np.array([1,2,3])+np.array([4,5,6])   # numpy를 이용하면 가능, 단 연산하려는 대상 간 사이즈가 같아야함

# 5. 형(데이터 타입) 변환 메소드
a2.astype('float')
a2.astype('int')
a2.astype('str')

# 6. np.where 함수
# if문의 축약
# np.where(조건, 참인 값 반환, 거짓인 값 반환)

# sql 문 기본 형태 : select * from db where

np.where(a2>5,'A','B')

# 7. 산술 연산 메소드
a2.sum()  # 합
a2.mean()   # 평균
a2.var()   # 분산
a2.std()  # 표준편차
a2.min()  # 최소값
a2.max()  # 최대값

(a2>5).sum()  # a2에서 5보다 큰 값의 개수
(a2>5).any()  # a2에서 5보다 큰 값 하나라도 있을 경우 참
(a2>5).all()  # a2에서 5보다 모든 값이 클 경우만 참

a2
a2.sum(axis=0)  # 행 기준, 열끼리 더한 값(서로 다른 행끼리 , 즉 행 별 총합, 세로방향 연산)
a2.sum(axis=1)  # 열 기준, 행끼리 더한 값(서로 다른 열끼리 , 즉 열 별 총합, 가로방향 연산) 

# [축 번호] >>> 자칫하면 헷갈리니 확실하게 짚고 넘어갈 것
# 2차원 : 행(0), 열(1)
# 3차원 : 층(0), 행(1), 열(2)


# 8. 전치(transpose) 메소드(행과 열을 서로 바꿈)
# 1) T : 행과 열을 전치
a1=np.arange(1,9).reshape(4,2)
a1.T
# 2) swapaxes : 두 축을 전달 받아서 두 축을 서로 전치
a1
a1.swapaxes(0,1)
a1.swapaxes(1,0) # (0,1)과 같은 결과, 전달 순서는 중요하지 않음

# 3) transpose : 원본의 차원에 맞는 축번호를 인수에 차례대로 전달 후, 그대로 전치
a1.transpose(0,1)  # 원본 그대로 출력
a1.transpose(1,0) # (0,1)과 다른 결과, 행과 열 전치, 전달 순서 중요

# 외부 파일 입출력
# 1) 파일 불러오기
#  np.loadtxt(fname,      # 파일명
#             dtype,      # 데이터타입
#             delimiter,  # 필드 구분 기호
#             skiprows,   # skip 할 행의 수
#             usecols,    # 선택할 컬럼 값(위치)
#             encoding)   # 인코딩 옵션

import numpy as np
np.loadtxt('C:/Users/sjh73/Desktop/Code_SJH/data/file1.txt', delimiter=',', dtype='str')  # 경로에 \를 /로 바꿔야함
np.loadtxt('./data/file1.txt', delimiter=',', dtype='str')  # ./는 현재폴더, ../는 한단계위폴더

# 2) 파일 내려쓰기
# np.savetxt(fname,       # 파일명
#            X,           # 객체명
#            delimiter,   # 구분자
#            fmt,         # 출력형식(format)
#            header,      # 헤더 출력 여부(file 첫 문자열)
#            encoding)    # 인코딩 옵션
a2 = np.arange(1,15)
np.savetxt('C:/Users/sjh73/Desktop/Code_SJH/data/file2.txt', a2, delimiter=',', fmt='%s')
# '%s' : 문자타입(string)

# 참고 : fmt 전달/변경 방식
# %s : 문자열
# %f : 실수
# %d : 정수
'%s' % 123
'%f' % 123
'%0.2f' % 123
'%d' % 123
'%10d' % 123







