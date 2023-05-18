"""
단순 연결 리스트 생성 간결화
"""

##전역 변수 설정##
memory= [] #주소 값 저장하는 리스트 생성
head, current, pre = None, None, None
dataArray=['다현','정연','쯔위','사나','지효']


class node():
    def __init__(self):       
        self.data= None
        self.link= None   #링크드 리스트 생성에 있어 인스턴스화가 필요하기 때문에 __init__ 선언


def printNodes(start):     #링크드 리스트의 모든 내용 출력 함수
    current = start        

    if current == None:
        return
    
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

##메인코드부분##
if __name__ == '__main__':
    
    first = node()
    first.data= dataArray[0]
    head= first
    memory.append(first)

    for i in dataArray[1:]:
        pre=first
        first= node()
        pre.link= first
        first.data=i
        memory.append(first)

    printNodes(head)
print(memory)




