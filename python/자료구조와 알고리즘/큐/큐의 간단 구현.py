## 전역 변수 설정##
SIZE= int(input('큐의 크기를 입력하시오= '))
Q= [None for _ in range(SIZE)]
front= rear= -1

def isQFull():
    global SIZE, Q, front, rear
    if(rear == SIZE-1):
        return True
    else:
        return False
    
def isQEmpty():
    global SIZE, Q, front, rear
    if(front == rear):
        return True
    else:
        return False
    
def enQ(data):
    global SIZE, Q, front, rear
    if(isQFull()):
        print('스택이 꽉참')
        return
    rear+=1
    Q[rear]= data


def deQ():
    global SIZE, Q, front, rear
    if(isQEmpty()):
        print('스택이 비었음')
        return None
    front +=1
    data= Q[front]
    Q[front]= None
    return data

def peek():
    if(isQEmpty()):
        print('스택이 비었습니다')
        return None
    return Q[front+1]

if __name__ == '__main__':

    select= input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==>')

    while True:
        if(select == 'i' or select =='I'):
            data= input('입력할 데이터를==> ')
            enQ(data)
            print('큐의 상태', Q)
        elif(select == 'E' or select =='e'):
            data= deQ()
            print('추출된 데이터 => ', data)
            print('현재 큐의 상태: ', Q)
        elif(select == 'V' or select =='v'):
            data= peek()
            print('다음으로 추출 될 데이터==>', data)
        elif(select == 'X' or select =='x'):
            print('종료')
            break
        else:
            print('입력이 잘 못 됌')
        select= input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==>')
        




