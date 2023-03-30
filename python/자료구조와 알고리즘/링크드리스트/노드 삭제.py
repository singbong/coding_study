"""
노드를 삭제하는 방법
"""

class Node():
    def __init__ (self):
        self.data= None
        self.link= None

node1 = Node()
node1.data='이'

node2 = Node()
node2.data='건'
node1.link = node2

node3= Node()
node3.data='호'
node2.link= node3

node4=Node()
node4.data='cute'
node3.link= node4

node1.link = node2.link
del[node2]


current= node1
print(current.data, end='')

while current.link != None:   #current에 저장된 노드의 link가 None이 뜰때까지 즉 그 연결리스트의 끝까지 계속 출력될 때까지 link link link 파고든다.
    
    current= current.link
    print(current.data, end='')
    