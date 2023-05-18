"""
N X M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
다음의 4X5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.
입력 예시:
00110
00011
11111
00000

"""

## DFS를 활용한 재귀적 풀이##
def DFS(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if graph[y][x] == 0:

        graph[y][x]= 1

        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y-1)
        DFS(x,y+1)
        return True
    return False

if __name__ == '__main__':
    n, m= map(int, input().split())
    
    # n, m= 5,4
    graph= []
    # graph= [
    #     [0,0,1,1,0],
    #     [0,0,0,1,1],
    #     [1,1,1,1,1],
    #     [0,0,0,0,0]
    # ]
    for i in range(n):
        graph.append(list(map(int, input())))
    
    count= 0

    for b in range(m):
        for a in range(n):
            if DFS(a, b) == True:
                count +=1

    print(count)













