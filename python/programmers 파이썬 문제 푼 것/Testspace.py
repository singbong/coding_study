def solution(numbers):
    answer = []
    for v in range(0,len(numbers)):
        for i in range(v+1, len(numbers)):
            if numbers[v]+numbers[i] not in answer:
                answer.append(numbers[v]+numbers[i])
            else:
                continue
    answer.sort()
    return answer

print(solution([2,1,3,4,1]))