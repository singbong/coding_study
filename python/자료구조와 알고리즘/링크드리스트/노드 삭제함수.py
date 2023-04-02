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

##링크드 리스트 모든 노드 출력 함수##
def printNodes(start):   
    current = start        

    if current == None:
        return
    
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

##링크드 리스트 삽입 함수##
def insertNode(find_data, insert_data):
    global memory, pre, head, current


    #가장 첫번째 노드의 data가 찾고자 하는 data와 일치#
    if find_data == head.data:
        new_node= node()
        new_node.data= insert_data
        new_node.link= head
        head= new_node
        memory.append(new_node)
        return


    current= head
    while current.link != None:
        pre = current
        current = current.link
        if find_data == current.data:
            new_node = node()
            new_node.data= insert_data
            new_node.link = current
            pre.link = new_node
            memory.append(new_node)
            return
    
    new_node = node()
    new_node.data = insert_data
    current.link= new_node

##노드 삭제 함수##

def deleteNode(find_data):
    global memory, pre, head, current

    if head.data == find_data:
        pre =head
        head = head.link
        memory.remove(pre)
        del(pre)
        return
    
    current = head
    while current.link != None:
        pre= current
        current = current.link
        if current.data == find_data:
            pre.link = current.link
            memory.remove(current)
            del(current)
            return
        


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

    deleteNode('쯔위')
    printNodes(head)
    
    for i in memory:
        print(i.data)

"""
memory에 저장된 주소값을 이용하여 뭘 할 수 있을가 찾아보다가 memory에 저장된 주소를 활용하여 각 노드의 link와 data를 출력 할 수 있는 것을
발견하였다. 근데 만약 링크드 리스트로 노드를 생성하고 값들을 저장하였는데 memory에 저장된 주소값을 활용하여 데이터를 찾거나 삭제하거나 추가한다면
일반 리스트와 달라질게 없는 것인가? 

궁금한것: 왜 memory의 값을 이용하여 값을 삭제하거나 추가하거나 찾지 않는지


이유를 찾아본 결과:
궁금한거는 왜 memory의 값을 이용하여 값을 삭제하거나 추가하거나 찾지 않는거야?
링크드 리스트에서 각 노드의 연결 관계는 노드의 주소 값을 이용하여 구현됩니다. 
이때, 각 노드의 주소 값을 메모리 상에 저장하기 위해 동적 메모리 할당을 사용하게 됩니다.

따라서, 링크드 리스트에서 노드를 추가하거나 삭제할 때는 해당 노드의 주소 값을 이용하여 연결 관계를 조정합니다. 
이를 위해 링크드 리스트의 각 노드는 자신의 주소 값과 다음 노드의 주소 값을 저장하는 링크(link) 변수를 가지고 있습니다.

따라서, 노드를 추가하거나 삭제할 때는 해당 노드의 링크 변수와 이전 노드의 링크 변수를 변경하여 연결 관계를 조정합니다. 
예를 들어, insertNode 함수에서는 새로운 노드를 생성한 후, 해당 노드의 링크 변수를 이전 노드의 링크 변수와 현재 노드의 링크 변수 
사이에 삽입하여 연결 관계를 형성합니다.

반면, memory 리스트는 생성된 모든 노드의 주소 값을 저장하는 역할을 합니다. 이를 활용하여, 생성된 모든 노드의 정보를 출력하거나, 
노드를 삭제할 때 해당 노드의 주소 값을 찾아 메모리에서 삭제하는 등의 역할을 수행합니다. 따라서, memory 리스트는 링크드 리스트의 
연결 관계를 조정하는데 직접적으로 사용되는 것은 아닙니다.




신봉균
그러면 memory 리스트를 이용하여 노드를 삭제하거나 삽입 찾는것은 링크드 리스트를 사용하는 본질에 어긋나는거야?
링크드 리스트는 동적 메모리 할당을 이용하여 노드들을 연결하여 구현되는 자료 구조입니다. 따라서, 링크드 리스트의 연결 관계를 
조정할 때는 각 노드의 링크(link) 변수를 이용하여 연결 관계를 수정해야 합니다.

반면에, memory 리스트는 각 노드의 주소 값을 저장하는 용도로 사용되며, 링크드 리스트에서의 연결 관계를 직접적으로 수정하는 데 
사용되는 것은 아닙니다. 따라서, memory 리스트를 이용하여 링크드 리스트의 연결 관계를 조정하는 것은 링크드 리스트의 본질과는 어긋나는 것입니다.

따라서, 링크드 리스트에서 노드를 삭제하거나 삽입하거나 찾을 때는 각 노드의 링크(link) 변수를 이용하여 연결 관계를 조정해야 
합니다. 이를 위해 링크드 리스트에서 노드를 추가하거나 삭제할 때는 해당 노드의 링크(link) 변수와 이전 노드의 링크(link) 변수를 
변경하여 연결 관계를 조정합니다. 또한, 노드를 찾을 때는 head부터 시작하여 각 노드의 링크(link) 변수를 따라가며 찾는 것이 일반적입니다.




신봉균
그러면 memory리스트를 사용하여 데이터를 찾는거와 링크드 리스트의 node의 link를 타고 데이터를 찾는 것중에 어떤게 속도가 더 빨라?
memory 리스트는 각 노드의 주소 값을 저장하는 리스트이므로, 해당 노드를 찾을 때는 리스트의 원소를 탐색하여 해당 노드의 주소 값을 
찾아야 합니다. 이는 선형 탐색으로 이루어지며, 최악의 경우 링크드 리스트의 길이에 비례하는 시간이 소요됩니다. 따라서, memory 리스트를 
이용하여 데이터를 찾는 것은 비효율적입니다.

반면에, 링크드 리스트의 각 노드는 링크(link) 변수를 이용하여 다음 노드의 주소 값을 가리키므로, 해당 노드를 찾을 때는 head부터 
시작하여 각 노드의 링크(link) 변수를 따라가면 됩니다. 이는 선형 탐색과 유사하지만, 리스트의 길이와 무관하게 일정한 시간이 소요됩니다. 
따라서, 링크드 리스트의 node의 link를 타고 데이터를 찾는 것이 효율적입니다.

"""