## 재귀 함수를 이용하여 팩토리얼 구현##

#5!= 5*4*3*2*1

def factorial_recursion(n):
    if n <= 1:
        return 1
    return n*factorial_recursion(n-1)

print(factorial_recursion(5))