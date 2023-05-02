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

def DFS(graph, a, visited):
    visited[a]= True
    print(a, end=' ')
    for i in graph[a]:
        if not visited[i]:
            DFS(graph, i, visited)





if __name__ == '__main__':
    visited = [False for _ in range(len(graph))]
    DFS(graph, 1, visited)

