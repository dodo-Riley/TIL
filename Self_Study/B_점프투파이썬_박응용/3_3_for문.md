# 3.3. for문

> `while`문과 마찬가지로 문장을 반복 수행할 때 사용하지만, `while`문은 조건문이 참일 경우에 한해 문장을 수행하고 `for`문은 주어진 범위의 변수에 대해 문장을 반복 수행한다.
> 

# **3.3.1. for문 기본 구조**

> 기본적으로 `for`문이 반복 수행할 범위가 존재해야하며, 해당 범위의 변수에 대해 문장을 반복 수행한다. `for`문의 기본 구조는 아래와 같다.
> 

```python
a = [1, 2, 3, 4, 5]

for i in a:
	print(i+1)

→2
3
4
5
6
```

리스트 `a`에 속하는 `1, 2, 3, 4, 5` 각각에 대해 `+1`을 한 뒤 출력하는 결과를 보여준다. 변수는 숫자뿐만 아니라 문자열이나 튜플 등의 자료형도 가능하다.

# **3.3.2. for문 활용 예시**

- 5명의 사람에 대한 신장(키) 정보가 주어지고, 키가 180이상이면 큰 편, 165이상 180미만이면 보통, 165미만은 작은 편이라는 값을 출력하도록 해보자.
    
    ```python
    tall = [155, 167, 175, 181, 188]
    num = 0
    
    for k in tall:
    	num = num+1
    	if k >= 180:
    		print('%d번은 큰 편입니다.' % num)
    	elif 165 <= k < 180:
    		print('%d번은 보통입니다.' % num)
    	else:
    		print('%d번은 작은 편입니다.' % num)
    
    → 1번은 작은 편입니다.
    2번은 보통입니다.
    3번은 보통입니다.
    4번은 큰 편입니다.
    5번은 큰 편입니다.
    ```
    

# **3.3.3. continue/range/중첩 루프**

- **continue**
    
    `while`문과 마찬가지로 `continue`를 사용해 도중에 처음부터 다시 수행하도록 만들 수 있다. 위의 예시에서 키가 큰 편인 사람의 결과만 출력되도록 하려면 `continue`를 사용해 아래와 같이 가능하다.
    
    ```python
    tall = [155, 167, 175, 181, 188]
    num = 0
    
    for k in tall:
    	num = num+1
    	if k < 180:
    		continue
    	print('%d번은 큰 편입니다.' % num)
    
    → 4번은 큰 편입니다.
    5번은 큰 편입니다
    ```
    

.

- **range**
    
    `for`문은 반복 수행할 대상이 필요하기 때문에, 숫자 리스트를 자동으로 만들어 주는 `range` 함수와 자주 함께 사용된다. `range(start, stop, step)`의 형태로 사용하며 끝 숫자는 포함되지 않는다. 즉 `시작 숫자 이상, 끝 숫자 미만`의 값이 포함된다. 이전의 키 정보에 대한 예시를 `range`를 활용하면 아래와 같으며 결과는 동일하다.
    
    ```python
    tall = [155, 167, 175, 181, 188]
    
    for k in range(len(tall)):
    	if tall[k] >= 180:
    		print('%d번은 큰 편입니다.' % (k+1))
    	elif 165 <= tall[k] < 180:
    		print('%d번은 보통입니다.' % (k+1))
    	else:
    		print('%d번은 작은 편입니다.' % (k+1))
    
    → 1번은 작은 편입니다.
    2번은 보통입니다.
    3번은 보통입니다.
    4번은 큰 편입니다.
    5번은 큰 편입니다.
    ```
    

- **중첩 루프**
    
    `for`문 안에 또 다른 `for`문을 넣어 이중 반복문 구조를 만들 수 있다. 예를 들어 `[1, 2, 3]`과 `[a, b, c]`, 2개의 리스트를 활용해 중첩 루프 구조를 만들면, 문장의 반복 수행은 1a, 1b, 1c, 2a, 2b, 2c, 3a, 3b, 3c순으로 진행된다. 이를 활용하면 구구단을 출력할 수 있다.
    
    ```python
    for a in range(1,10):
    	for b in range(1,10):
    		print(a, 'x', b, '=', a*b)
    ```
    
    (참고 : [https://tali.tistory.com/1302](https://tali.tistory.com/1302))
    

# **3.3.4. 리스트 내포**

> `for`문은 리스트 안에 포함될 수 있으며, 이를 리스트 내포라고 한다.
> 

- `for`문의 결과를 리스트에 담고 싶다면 빈 리스트를 생성하고 요소를 추가하면 된다. 아래 예시는 각 요소에 3을 곱한 값을 요소로 가지는 리스트를 출력한다.
    
    ```python
    a = [1, 2, 3, 4]
    result = []
    
    for i in a:
    	result.append(i*3)
    	
    print(result)
    
    → [3, 6, 9, 12]
    ```
    

- 이와 다르게 리스트 내포를 활용하면 좀 더 편리하다. 위의 예시를 리스트 내포를 사용하면 아래와 같으며 결과는 동일하다.
    
    ```python
    a = [1, 2, 3, 4]
    result = [i*3 for i in a]
    print(result)
    
    → [3, 6, 9, 12]
    ```
    

- 이 때, `if` 조건을 붙여 조건에 해당되는 요소에 대해서만 수행하도록 할 수 있다.
    
    ```python
    a = [1, 2, 3, 4]
    result = [i*3 for i in a if i%2==1]
    print(result)
    
    → [3, 9]
    ```
    

- 중첩 루프와 같이 for문을 2개 이상 사용하는 것도 가능하다.
    
    ```python
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8, 9]
    result = [x*y for x in a
                  for y in b]
    print(result)
    
    → [5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 15, 18, 21, 24, 27, 20, 24, 28, 32, 36]
    ```