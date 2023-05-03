from collections import deque

# BFS 함수 정의
def bfs(x, y):
    q = deque([(x, y)])
    # 현재 위치를 방문 처리
    if graph[y][x] == 1:
        return False
    graph[y][x] = 1
    
    while q:
        data= q.popleft()
        if y-1 >=0:
            q.append(graph[y-1][x])
        if y+1 < m:
            q.append(graph[y+1][x])
        if x-1 >= 0:
            q.append(graph[y][x-1])
        if x+1 < n:    
            q.append(graph[y][x+1])


# 입력 받기
# n, m = map(int, input().split())
n,m= 5,4

graph= [
        [0,0,1,1,0],
        [0,0,0,1,1],
        [1,1,1,1,1],
        [0,0,0,0,0]
    ]
# for i in range(n):
#     graph.append(list(map(int, input())))

# BFS 알고리즘으로 아이스크림 개수 구하기
result = 0
for i in range(n):
    for j in range(m):
        if bfs(j, i) == True:
            result += 1

# 결과 출력
print(result)