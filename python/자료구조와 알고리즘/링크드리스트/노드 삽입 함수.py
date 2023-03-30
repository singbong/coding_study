"""
단순 연결 리스트의 노드 삽입 함수
"""

##전역 변수 설정##
memory= [] #주소 값 저장하는 리스트 생성
head, current, pre = None, None, None
dataArray=['다현','정연','쯔위','사나','지효']


class node():
    def __init__(self):
        self.data= None
        self.link= None


#노드 출력 함수#

def printNodes(start):
    current = start
    
    if current == None:
        return
    
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

##노드 삽입 함수##
def insertNode(find_data, insert_data):
    global memory, head, pre, current
     
    if head.data == find_data:   #맨 앞의 data가 찾고자하는 데이터와 같으면
        first= node()
        first.data = insert_data #새로운 노드 생성 후 새 노드에 넣고자하는 값 입력
        first.link = head        #새로운 노드가 head이기 때문에 새노드의 link는 이전 head를 가리킴
        head= first              #link 세팅이 끝났음으로 새노드를 head로 지정
        return
    
    current= head                 # 맨앞에서부터 링크드 리스트를 훑을거기 떄문에 current가 head이다
    while current.link != None:   #노드가 끝낼때까지 반복
        pre= current              #current를 pre에 백업 시키는 개념
        current = current.link    #current 데이터를 싹 날리고 current.link(current 다음 노드)로 업데이트
        if current.data == find_data:   #current data가 찾고자하는 데이터와 일치하면
            first = node() 
            first.data = insert_data   #노드를 생성 후 넣고자하는 데이터를 새 노드 데이터에 입력
            first.link = current       # 새노드의 link를 current로 지정
            pre.link = first           #맨처음 current의 값을 백업 해둔 pre의 link를 새로 생성시킨 노드를 가리키게끔 한다.
            return
        
    first = node()                     #위에 코드를 다 실행 했는데도 여기 까지 온거면 일치하는 데이터가 없는 것임으로 맨끝에 노드 생성후 추가
    first.data= insert_data
    current.link= first


##메인 함수 부분##
if __name__ == '__main__':
    
    first = node()
    first.data= dataArray[0]
    head= first
    memory.append(first)
    

    for i in dataArray[1:]:
        pre=first
        first = node()
        first.data=i
        pre.link= first
        memory.append(first)

    insertNode('', '봉균')
    printNodes(head)













