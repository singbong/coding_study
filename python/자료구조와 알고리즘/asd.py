from collections import deque

def bfs(x, y):
    global graph
    q = deque([(x, y)])
   
    if graph[y][x] == 1:
        return False
    
    while q:
        a= q.popleft()
        x, y = a[0], a[1]
        if graph[y][x] == 0:
            graph[y][x] = 1
            if y-1 >=0:
                q.append((x, y-1))
            if y+1 < m:
                q.append((x, y+1))
            if x-1 >= 0:
                q.append((x-1, y))
            if x+1 < n:    
                q.append((x+1, y))
    return True

n,m= 5,4

graph= [
        [0,0,1,1,0],
        [0,0,0,1,1],
        [1,1,1,1,1],
        [0,0,0,0,0]
    ]

result = 0
for i in range(m):
    for j in range(n):
        if bfs(j, i) == True:
            result += 1

print(result)