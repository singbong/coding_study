## 전역 변수 설정##
SIZE= int(input('큐의 크기를 입력하시오'))
Q= [None for _ in range(SIZE)]
front= rear= -1

def isQFull():
    global SIZE, Q, front, rear
    if(rear>=SIZE-1):
        return True
    else:
        return False
    
def isQEmpty():
    global SIZE, Q, front, rear
    if(rear == -1):
        return True
    else:
        return False
    
def enQ(data):
    global SIZE, Q, front, rear
    if(isQFull):
        print('스택이 꽉참')
        return
    rear +=1
    Q[rear]= data

def deQ():
    global SIZE, Q, front, rear
    if(isQEmpty):
        print('스택이 비었음')
        return None
    data= Q[front]
    Q[front]= None
    front -=1
    return data

