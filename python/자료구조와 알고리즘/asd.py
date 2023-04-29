def isQEmpty():
    global SIZE,q, front, rear
    if (front == rear):
        return True
    else:
        return False
    
def isQFull():
    global SIZE,q, front, rear
    if (rear == SIZE-1):
        return True
    else:
        return False
    
    
def enQ(data):
    global SIZE,q, front, rear
    if (rear == SIZE-1):
        print('큐 꽉참')
        return
    rear +=1
    q[rear]= data
    
    
def deQ():
    global SIZE,q, front, rear
    if(isQEmpty()):
        print('큐가 비었습니다.')
        return None
    front +=1
    data= q[front]
    q[front]= None
    return data
    
    
def peek():
    global SIZE,q, front, rear
    if(isQEmpty()):
        print('큐가 비었습니다')
        return None
    return q[front+1]

##전역 변수 선언 부분##
SIZE= int(input('큐 크기를 입력하세요 ==>'))
q = [None for _ in range(SIZE)]
front= rear= -1

## 메인 함수 선언 부분##
if __name__ == '__main__':
    select= input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==>')
    
    while (select != 'X' and select != 'x'):
        if select == 'I' or 'i':
            data= input('입력할 데이터 ==>')
            enQ(data)
            print('큐 상태: ', q)
        elif select == 'E' or select=='e':
            data= deQ()
            print('추출된 데이터==>', data)
            print('큐 상태:', q)
        elif select == 'V' or select=='v':
            data= peek()
            print('확인된 데이터 ==>', data)
            print('큐 상태: ', q)
        else:
            print('입력이 잘못됨')

        select= input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==>')
    
    print('프로그램 종료!')
    
    
    
    