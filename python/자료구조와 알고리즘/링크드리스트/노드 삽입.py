"""
노드를 생성하고 해당 노드를 중간삽입
"""

# 노드 삽입

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

new_node= Node()     
new_node.data = 'very' #노드를 생선한후 추가하고 싶은 데이터를 생선한 노드의 data값에 저장후 생성
node3.link= new_node #끼워 넣고 싶은 곳의 앞의 노드의 link를 새로 생성한 노드를 가리키게 한다
new_node.link= node4 #노드의 link를 끼워넣고 싶은 곳 뒤에 있는 노드를 지정하여 linkd list를 완성

current= node1


while current.link != None:   #current에 저장된 노드의 link가 None이 뜰때까지 즉 그 연결리스트의 끝까지 계속 출력될 때까지 link link link 파고든다.

    current= current.link
    print(current.data, end='')

