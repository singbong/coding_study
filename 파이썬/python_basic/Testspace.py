def solution(n, arr1, arr2):
    result= list()
    for i in range(0,n):
        v1= list(bin(arr1[i])[2:])
        v2= list(bin(arr2[i])[2:])
        if len(v2) < n:
            for k in range(0,(n-len(v2))):
                v2.insert(0, '0')
        if len(v1) < n:
            for l in range(0,(n-len(v1))):
                v1.insert(0, '0')
        a= ''.join(v1)
        b= ''.join(v2)
        print(a, b)
        s1= str()
        for v in range(0, len(a)):
            if int(a[v])+int(b[v]) == 0:
                s1= s1 + ' '
            else:
                s1 = s1 + '#'
        result.append(s1)
    return result

print(solution(	6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
