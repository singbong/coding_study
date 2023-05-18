##링크드 리스트를 활용한 명함 관리 프로그램##

##전역변수##
memory= []
pre, head, current = None, None, None
data_array= [['지민','010-1111-2222'],['정국','010-2222-2222'],['뷔','010-3333-3333'],['슈가','010-4444-4444'],['진','010-5555-5555']]

##노드 생성 클래스##

class node():
    def __init__(self):
        self.data= None
        self.link= None
##링크드 리스트 출력 함수##
def printNodes(start):
    current= head
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current= current.link
        print(current.data, end=' ')
    print()

##이름 순서대로 정렬해주는 함수##

def orderNodes(i):
    global pre, current, head, memory

    first= node()
    first.data= i
    memory.append(first)
#노드가 아예 존재하지 않을때#
    if head == None:
        head= first
        return
#노드의 순서가 양쪽 맨 끝이 아닐때#
    if first.datas[0] < head.data[0]:
        first.link= head
        head= first
        return
    
    current= head
    while current.link != None:
        pre= current
        current= current.link
        if i[0] < current.data[0]:
            pre.link = first
            first.link = current
            return
#노드가 순서가 맨 끝에 있을때#
    current.link= first
    


##메인 함수##

if __name__ == '__main__':
    for i in data_array:
        orderNodes(i)    
    printNodes(head)




