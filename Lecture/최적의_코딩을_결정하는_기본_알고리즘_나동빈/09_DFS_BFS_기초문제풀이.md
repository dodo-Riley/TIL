# 9. 그래프 탐색 실습 : DFS와 BFS 기초 문제풀이

- 음료수 얼려먹기 문제
    - 문제
        - N X M 크기의 얼음 틀이 존재.
        - 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시
        - 구멍이 뚫려 있는 부분끼리 상하좌우로 붙어있는 경우, 서로 연결된 것으로 간주
        - 얼음 틀의 모양이 주어졌을 때, 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성
        - 다시 말해, 서로 연결된 덩어리의 갯수를 구하는 것
        - N과 M은 1이상 1000이하
    - DFS 활용 알고리즘
        - 특정 지점의 상하좌우 중, 값이 ‘0’이면서 방문하지 않은 지점이 있다면 해당 지점을 방문
        - 이를 반복해 연결된 모든 지점을 방문
        - 모든 노드에 대하여 위 과정을 반복, 방문하지 않은 지점의 수를 카운트
        
        ```python
        # DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
        def dfs(x,y):
        	# 주어진 범위를 벗어나는 경우에는 즉시 종료
        	if x <= -1 or x >= n or y <= -1 or y >= m:
        		return False
        	# 현재 노드를 아직 방문하지 않았다면
        	if graph[x][y] == 0:
        		# 해당 노드 방문 처리
        		graph[x][y] =1
        		# 상하좌우의 위치들도 모두 재귀적으로 호출
        		dfs(x-1, y)
        		dfs(x, y-1)
        		dfs(x+1, y)
        		dfs(x, y+1)   # 한 지점에 연결된 모든 노드들을 방문 처리
        		return True   # 한 지점에 연결된 모든 노드들을 방문 처리 했을때만 리턴됨
        	return False
        
        # N,M을 공백을 기준으로 구분하여 입력
        n,m = map(int, input().split())
        
        # 2차원 리스트의 맵 정보 입력 받기
        graph = []
        for i in range(n):
        	graph.append(list(map(int, input())))
        
        # 모든 노드에 대하여 음료수 채우기
        result = 0
        for i in range(n):
        	for j in range(m):
        		# 현재 위치에서 DFS 수행
        		if dfs(i,j) == True:
        			result += 1
        
        print(result)
        
        # 4 5
        # 00110
        # 00011
        # 11111
        # 00000
        # 3
        ```
        
    
- 미로 탈출
    - 문제
        - N X M 형태의 미로에 갇힌 상태
        - 현재 위치는 (1,1)이며 출구는 (N,M)이고 한 번에 한 칸씩 이동할 수 있음
        - 괴물이 있는 부분은 0, 없는 부분은 1이며 괴물을 피해야함
        - 탈출하기 위해 움직여야 하는 최소 칸의 개수는?(시작 칸과 마지막 칸을 모두 포함)
        - N과 M은 4이상 200이하
    - BFS 활용 알고리즘
        - (1,1)에서 시작
        - 상하좌우로 탐색을 진행하여 옆 노드를 방문하고 방문한 노드의 값을 이전 노드의 값+1로 변경
    
    ```python
    from collections import deque
    
    # BFS 구현
    def bfs(x,y):
    	# 큐 구현을 위해 deque 라이브러리 사용
    	queue = deque()
    	queue.append((x,y))
    	# 큐가 빌 때까지 반복
    	while queue:
    		x,y = queue.popleft()
    		# 현재 위치에서 상하좌우로 확인
    		for i in range(4):
    			nx = x + dx[i]
    			ny = y + dy[i]
    			# 미로 찾기 공간을 벗어난 경우 무기
    			if nx < 0 or nx >= n or ny < 0 or ny >= m:
    				continue
    			# 벽인 경우 무시
    			if graph[nx][ny] == 0:
    				continue
    			# 해당 노드를 처음 방문하는 경우에만 +1 기록
    			if graph[nx][ny] == 1:
    				graph[nx][ny] = graph[x][y]+1
    				queue.append((nx,ny))
    	# 가장 오른쪽 아래까지의 최단거리 반환
    	return graph[n-1][m-1]
    
    # N,M을 공백으로 구분하여 입력
    n,m=map(int, input().split())
    # 2차원 리스트의 맵 정보 입력 받기
    graph = []
    for i in range(n):
    	graph.append(list(map(int, input())))
    
    # 이동할 네 가지 방향 정의
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    # 결과 출력
    print(bfs(0,0))
    ```