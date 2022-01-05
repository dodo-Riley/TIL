# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:37:21 2021

@author: sjh73
"""

# 조건문과 반복문

# 논리연산자
# and
# or
# not

v1=1
(v1>=3) and (v1<=7)  # 3과 7 사이
(v1>=3) & (v1<=7)    # 3과 7 사이

(v1<=3) or (v1>=7)
(v1<=3) | (v1>=7)

not(v1==1)

# 조건문 if
# 형식 
# if 조건:
#     참(true)일 때 실행 문장
# else:
#     거짓(false)일 대 실행 문장

# if 조건1:
#     조건 1이 참(true)일 때 실행 문장
# elif 조건2:
#     조건1이 거짓이면서 조건 2가 참일 때 실행 문장
# else:
#     조건1,2가 모두 거짓(false)일 대 실행 문장

v1=10

if v1>5:
    print('A')
else:
    print('B')
    
# list는 불가 
l1 = [1,2,3,4,5]
if l1>5:
    print('A')
else:
    print('B')
    
# 반복문
# 객체의 각 원소에 동일한 연산처리 진행할 경우 사용
# 1. for 문 : 정해진 횟수, 대상이 있을 경우 사용

# for 반복변수 in 반복할 대상(범위):
#     반복 실행할 문장

# 1-10까지 출력하기
range(1,11)

for i in range(1,11):
    print(i)
    
#예제
# 다음의 리스트 선언하고 5보다 클 경우 'A', 적거나 같을 경우 'b'

l1 = [1,3,5,15,25]

for i in l1:
    if i>5:
        print('A')
    else:
        print('B')
        
# 위 리스트에서 각 원소에 10을 더해서 출력
l1 + 10  # 불가능

for i in l1:
    print(i+10)
    
# for문은 결과를 바로 변수로 저장하는 것이 불가

l2 = for i in l1:
    print(i+10)       # 불가능
    
# 하는 법?  
l2 = []               # 빈 리스트 생성
for i in l1:
    l2.append(i+10)
print(l2)

l2 = [i+10 for i in l1]
print(l2)

# while 문 : 조건에 따른 반복을 실행하는 경우 사용
# while 조건:
#      조건이 참일 경우, 반복 문장
    
# 예제
# while 문으로 1~10까지 출력

i=1
while i <=10:
    print(i)
    i=i+1        # 이 부분이 없으면 멈추기 전까지 반복해서 1 출력

# 예제
# 1~100 까지 총 합은?

vsum = 0
for i in range(1,101):
    vsum = vsum + i
print(vsum)
    
# i     vsum       일반화
# 1     1          vsum+1
# 2     1+2        vsum+2
# 3     1+2+3      vsum+3
# 4     1+2+3+4    vsum+4
# ......
# i     1+2+,,,+i  vsum+i

vvvv= sum(i for i in range(1,101))
print(vvvv)

# 1~100까지 짝수 총합

vsum = 0
for i in range(1,101):
    if i%2 == 0:
        vsum = vsum + i
    else:
        vsum = vsum
print(vsum)

# 반복제어문
# 1. continue : 특정 조건일 경우 반복문 스킵
# 2. break : 특정 조건일 경우 반복문 종료(정지조건)
# 3. exit : 특정 조건일 경우 프로그램 종료
# 4. pass : 문법적으로 오류가 발생하지 않도록 빈 자리를 채우는 역할

# 예제
# 1-10출력, 5제외
for i in range(1,11):
    if i == 5:
        continue
    print(i)
    
for i in range(1,11):
    if i==5:
        break
    print(i)
    
# for i in range(1,11):
#     if i==5:
#         exit(0)
#     print(i)

v1=1
if v1>=10:
    pass      # pass 없으면 오류남
else:
    print('b')
    
    
# 예제
# 1부터 100까지 누적합이 최초 2000이상이 되는 시점의 k 값과 총합을 출력

vsum=0
for i in range(1,101):
    vsum = vsum+i
    if vsum >=2000:
        break
print(i, vsum)

