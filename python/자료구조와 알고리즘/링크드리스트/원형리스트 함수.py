"""
링크드 리스트를 이용하여 원형리스트를 만든다.
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
    
    while current.link != None:
        current= current.link
        print(current.data, end=' ')
    print()

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

    printNodes(head)
    print(memory)