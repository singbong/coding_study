## 무한히 반복하는 재귀함수

def recursive_function(i):
    #100번째 호 출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i,'번째 재귀함수에서' , i+1,'번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다.')
    
recursive_function(1)

#스택과 매우 비슷한 구조