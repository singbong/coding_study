"""
링크드 리스트를 이용하여 원형리스트를 만들고 링크드 리스트에 노드를 삽입하는 함수를 만든다.
"""

###전역 변수##
memory= []
pre, head, current= None, None, None
data_array= ['가','나','다','라','마','바','사','아']


##노드 생성함수##
class node():
    def __init__(self):
        self.data= None
        self.link= None

##노드 출력 함수##
def printNodes(start):
    current= start
    if current.data == None:
        return
    print(current.data, end=' ')
    
    while current.link != start:
        current= current.link
        print(current.data, end=' ')
    print()

##원형리스트 삽입##
def insertData(find_data, insert_data):
    global memory, current, pre, head
    
    
    if head.data == find_data:      #찾고자하는 노드가 head부분에 있을때
        first= node()
        memory.append(first)
        first.data= insert_data
        first.link= head
        current= head
        while current.link != head:  #가장 마지막노드는 아직 새로 생긴 노드를 가르키지 않기 때문에 current를 마지막 노드에 배치시키는 역할
            current= current.link
        head= first             #새로 생성한 노드를 head라 업데이트
        current.link = head     #마지막노드를 새로운 head를 가르키게끔 설정
        return
    
    current = head
    while current.link != head:          #찾고자하는 노드가 중간에서 발견되었을때
        pre= current
        current= current.link
        if current.data == find_data:  #찾고자하는 노드 찾았을때 노드 끼워넣기
            first= node()
            first.data= insert_data
            pre.link= first
            memory.append(first)
            first.link= current
            return
        
    first= node()                  #찾고자하는 노드가 없을때는 마지막 노드에 넣고자하는 데이터를 노트화 해서 삽입한다.
    first.data = insert_data
    memory.append(first)
    current.link= first
    first.link=head
        

##메인 함수##

if __name__ == '__main__':
    first= node()
    first.data= data_array[0]
    head= first
    first.link= head
    memory.append(first)

    for i in data_array[1:]:
        pre= first
        first= node()
        memory.append(first)
        pre.link= first
        first.data=i
        first.link= head

    insertData('삭','발')
    printNodes(head)
    