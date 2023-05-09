from collections import deque

graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited= [None for _ in range(len(graph))]

def BFS(graph, v, visited):
    q= deque([v])
    visited[v]= True

    while q:
        a= q.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if not visited[i]:
                q.append(i)
                visited[v]=True
                
                

            
BFS(graph, 1, visited)



