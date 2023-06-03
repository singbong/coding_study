class Grpaph():
    def __init__ (self, size):
        self.SIZE= size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1= None
stack= []
visitedAry= []

G1= Grpaph(4)
G1.graph[0][2]=1; G1.graph[0][3]=1
G1.graph[1][2]=1
G1.graph[2][0]=1; G1.graph[2][1]=1; G1.graph[2][3]=1
G1.graph[3][0]=1; G1.graph[3][2]=1

print('##G1 무방향 그래프')
for i in range(4):
    for j in range(4):
        print(G1.graph[i][j], end=' ')
    print()

current= 0
stack.append(current)
visitedAry.append(current)

while(len(stack)):
    