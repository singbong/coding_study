##DFS= Deep First Search를 재귀함수가 아닌 while 반복문으로 구현##

##노드##

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def DFS(graph, v, visited):
    stack= [v]
    while stack:
            data= stack.pop()
            if not visited[data]:
                visited[data]= True
                print(data, end=' ')
                for i in range(len(graph[data])-1,-1,-1):
                    stack.append(graph[data][i])
                     
"""
def DFS(graph, start, visited):
    stack = [start]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            stack += reversed(graph[v])
"""




if __name__ == '__main__':
    visited= [False for _ in range(len(graph))]
    DFS(graph, 1, visited)