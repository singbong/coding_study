"""
버블 정렬
"""
def solution(x):
    for k in range(0, len(x)-1):
        for b in range(0, len(x)-k-1):
            if x[b] > x[b+1]:
                x[b], x[b+1] = x[b+1], x[b]
    return x

print(solution([4,5,6,3,2,1]))

                







