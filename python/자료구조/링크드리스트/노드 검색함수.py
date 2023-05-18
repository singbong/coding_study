##전역 변수##
pre, head, current= None, None, None
memory= []
data_array= ['가','나','다','라']

##노드 생성함수##

class node():
    def __init__(self):
        self.data= None
        self.link= None

##노드 출력 함수##
def printNodes(start):
    current = head
    if current == None:
        return
    
    print(current.data, end=' ')
    while current.link != None:
        current=current.link
        print(current.data, end=' ')
    print()

##노드 삽입 함수##
def insertData(find_data, insert_data):
    global pre, current, memory, head

    if head.data == find_data: #찾는 노드가 head에 있을때
        first=node()
        first.data= insert_data
        first.link=head
        first=head
        memory.append(first)
        return
    
    current= head
    while current.link != None: #찾는 노드가 중간에 있을때
        pre= current
        current=current.link
        if current.data == find_data:
            first= node()
            first.data= insert_data
            first.link= pre.link
            pre.link= first
            memory.append(first)
            return
    
    #위에 코드를 모드 실행했는데 찾고자 하는 노드를 못찾았다면 존재하지 않기에 마지막에 추가
    first= node()
    first.data= insert_data
    current.link= first
    memory.append(first)
    return

##검색 함수##

def findData(find_data):
    global memory, pre, head, current

    current = head
    if current.data == find_data:
        return current
    
    while current.link != None:
        current=current.link
        if current.data == find_data:
            return current
        
    return node()






##메인함수##
if __name__ == '__main__':
    first= node()
    first.data= data_array[0]
    memory.append(first)
    head= first

    for i in data_array[1:]:
        pre= first
        first= node()
        first.data= i
        pre.link= first
        memory.append(first)
    printNodes(head)

    insertData('람','헐')
    printNodes(head)
