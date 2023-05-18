"""
(문제) 상하좌우

여행가 A는 N*N 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1*1크기의 정사각형으로 나누어져
있습니다. 가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당합니다.
여행가 A는 상,하,좌,우 방향으로 이동 할 수 있으며, 시작 좌표는 항상 (1,1)입니다. 우리 앞에는
여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.

계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D 중 하나의 문자가 반복적으로 적혀 있습니다.
각 문자의 의미는 다음과 같습니다.

L= 왼쪽으로 한칸이동
R= 오른쪽으로 한칸이동
U= 위로 한칸 이동
D= 아래로 한칸 이동
"""
# N = int(input())
# plan = list(input().split())
# start= (1,1)

# for i in plan:
#     if i == 'R' and start[-1] < N:
#         start= [start[0],start[-1]+1]
#     if i == 'L' and start[-1] > 1:
#         start= [start[0],start[-1]-1]
#     if i == 'U' and start[0] > 1:
#         start= [start[0]-1,start[-1]]
#     if i == 'D' and start[0] < N:
#         start= [start[0]+1,start[-1]]

# print(start)

###########################################################################
#N 입력 받기
n= int(input())
x,y= 1,1
plans= input().split()

move_type= ['L', 'R', 'U', 'D'] #해당 움직임에 맞게 비교군 설정
dx=[0,0,-1,1]                   # L R U D가 입력되었을때 순으로 이동해야할 x
dy=[-1,1,0,0]                   #               "              이동해야할 y 

for i in plans:
    for v in range(0,len(move_type)):
        if i == move_type[v]:
            nx= x + dx[v]
            ny= y + dy[v]
    if nx < 1 or ny < 1 or nx > n or ny > n: #만약 범위를 벗어 난다면 무효한후 다음 plans의 인덱스로 넘어감
        continue
    x,y=nx,ny

print(x, y)
    










