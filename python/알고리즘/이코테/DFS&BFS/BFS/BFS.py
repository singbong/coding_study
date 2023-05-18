from collections import deque

graph =[
    ['start'],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
"""
def BFS(graph, a, visited):
    stack= deque()
    stack.append(a)
    while stack:
        v= stack.popleft()
        if not visited[v]:
            print(v, end=' ')
            if not visited[v]:
                visited[v]=True
                stack += graph[v]
"""

def BFS(graph, a, visited):
    stack= deque([a])
    visited[a]= True
    while stack:
        v= stack.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                stack.append(i)
                visited[i]= True


    

if __name__ == '__main__':
    visited= [False for _ in range(len(graph))]
    BFS(graph, 1, visited)