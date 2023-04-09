import random

class Node():
    def __intit__ (self):
        self.data=None
        self.link=None


def printNodes(start):
    current= start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current= current.link
        print(current.data, end=' ')
        print()

def countOddEven():
    global memory, head, current, current

    odd, even= 0, 0
    if head == None:
        return False
    
    current= head

    while True:
        if current.data % 2 ==0:
            even +=1
        else:
            odd +=1
        if current.link == head:
            break;
        current= current.link

    return odd, even


def makeZeroNumber(odd, even):
    if odd> even:
        reminder = 1
    else:
        reminder = 0
    current=head
    while True:
        if current.data %2==0:
            current.data *=-1
        if current.link == head:
            break
        current= current.link

##전역 변수 선언 부분##
memory=[]
head, current, pre= None, None, None

##메인 코드 부분##
if __name__ == '__main__':
    dataArray= []
    for _ in range(7):
        dataArray.append(random.randint(1,100))
    print(dataArray)
    
    node = Node()
    node.data= dataArray[0] 
    head= node
    node.link= head
    memory.append(node)
    
    oddCount, evenCount = countOddEven()
    print('홀수---->',oddCount,'\t','짝수---->',evenCount)
    
    
    makeZeroNumber(oddCount, evenCount)
    printNodes(head)