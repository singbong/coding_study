n= int(input())


class MakeOne():
    def __init__(self, x):
        self.x=x

    d= [0]*(n+1)

    def times(self):
        if self.x == 1:
            return MakeOne.d[1]
        for i in range(2, n+1):
            MakeOne.d[i]= MakeOne.d[i-1] +1
            if i%2==0:
                MakeOne.d[i]=min(MakeOne.d[i], MakeOne.d[i//2]+1)
            if i%3==0:
                MakeOne.d[i]=min(MakeOne.d[i], MakeOne.d[i//3]+1)
                
        return MakeOne.d[n]

result=MakeOne(n)
print(result.times())