def solution(number, limit, power):
    yaksu= list()
    for i in range(1,number+1):
        num=0
        for v in range(1,i+1):
            if i % v == 0:
                num+=1
            if num > limit:
                num= power
                break
        yaksu.append(num)
    return sum(yaksu)
print(solution(10,3,2))