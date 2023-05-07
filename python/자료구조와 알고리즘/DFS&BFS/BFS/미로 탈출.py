"""

* 동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이 있어 이를
  피해 탈출 해야합니다.
* 동빈이의 위치는 (1,1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니
  다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출할
  수 있는 형태로 제시됩니다.
* 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 칸을 셀 때는 시작 칸과 마지막
  칸을 모두 포함해서 계산합니다.

"""

from collections import deque

graph =[
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]
n= 5
m= 6

def BFS(graph):
    q= deque([(0,0)])
    count = 0
    while q:
        out= q.popleft()
        x,y = out
        a= graph[x][y]
        
        if x+1 <= 4:
            if graph[x+1][y] ==1:
                q.append((x+1, y))
                graph[x+1][y] = graph[x][y]+1
        if x-1 >= 0:
            if graph[x-1][y] ==1:
                q.append((x-1, y))
                graph[x-1][y] = graph[x][y]+1
        if y+1 <= 5: 
            if graph[x][y+1] == 1:
                q.append((x, y+1))
                graph[x][y+1] = graph[x][y]+1
        if y-1 >= 0:
            if graph[x][y-1] == 1:
                q.append((x, y-1))
                graph[x][y-1] = graph[x][y]+1

    print(graph)
    return graph[n-1][m-1]

print(BFS(graph))






