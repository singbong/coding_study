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

    insertNode('쯔위', '봉균')
    printNodes(head)


#메인 함수 부분에 for문에 대해서 보통 for문의 반복문이 끝나면 for문 밖으로는 for문 안의 변수들의 값이 날라간다. 이것은 for문 안의 변수들이
#call by value 즉 파이썬에서 불변형 자료 일 경우 해당된다 값이 날라가지 않는 경우는 call by reference인 경우 즉 가변형자료일 경우이다.
#가변형 자료일 경우 해당 값을 duplicate(복사) 하는 것이 아니라 해당변수가 저장된 주소를 가르키기 때문이다. 그렇다면 노드를 생성하는 node 함수에서
#진행되는 인스턴스화는 파이썬의 리스트나 딕셔너리처럼 가변형 데이터로 취급되는가

#리스트형이여도 a=[1], b=[] a=b b=[1,2,3] 이경우 a의 값이 [1,2,3]으로 변하지 않는다. 꼭 append같은것을 사용해주었을때만 a값이 변한다.
#그렇다면 아무리 가변형자료인 리스트 딕셔너리여도 윗 줄의 b=[1,2,3] 처럼 값을 업데이트는 방식이 아닌 append함수의 업데이트 방식을 사용
#하여 데이터를 복사하는 것이 아닌 데이터를 기존거에서 변형을 시킨다는 개념이 들어가야만 하는 것인가? 그것에 
#따라서 call by reference인지 call by value를 결정 짓는것인가?










