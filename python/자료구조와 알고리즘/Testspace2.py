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
                graph[x+1][y] = graph[x][y] +1
                
        if x-1 >= 0:
            if graph[x-1][y] ==1:    
                q.append((x-1, y))
                graph[x-1][y] = graph[x][y] +1
                
        if y+1 <= 5: 
            if graph[x][y+1] == 1:   
                q.append((x, y+1))
                graph[x][y+1] = graph[x][y] +1
                
        if y-1 >= 0:    
            if graph[x][y-1] == 1:
                q.append((x, y-1))
                graph[x][y-1] = graph[x][y] +1
                

    return graph


print(BFS(graph))

    

