n= int(input())

arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

d= [0]*(n+2)

for i in range(n-1, -1, -1):
    t= arr[i][0]
    p= arr[i][1]

    if i+t > n:
        d[i]= d[i+1]
    else:
        d[i]= max(d[i+1],d[i+t]+p)

print(d[0])

 