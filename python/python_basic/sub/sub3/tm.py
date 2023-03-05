
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x / y

def power(x, y):
    return x**y

#__name__ 사용

if __name__ == '__main__':
    print('-'*15)
    print('call! __main__')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(10,10))
    print(divide(10,5))
    print(power(2,5))
    print('-'*15)