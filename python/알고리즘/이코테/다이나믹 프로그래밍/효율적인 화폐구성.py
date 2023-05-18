

n = int(input())

numbers= list(map(int,input().split()))

class BTU():
    d= [10001]*(n+1)

    def __init__(self,x):
        self.x = x

    def times(self):

        if self.x == 0:
            return 0
        
        BTU.d[0]=0

        for num in numbers:
            for index in range(num,len(BTU.d)):
                if BTU.d[index-num] != 10001:
                    BTU.d[index]= min(BTU.d[index]+1,BTU.d[index-num]+1)   

        if BTU.d[n] == 10001:
            return print(-1)
        else:
            return BTU.d[n]


result= BTU(7)

print(result.times())


