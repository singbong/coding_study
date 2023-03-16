def solution(X, Y):
    x_set = set(X)
    y_set = set(Y)
    common_set = x_set & y_set
    if not common_set: # X, Y에 공통된 숫자가 없을 경우
        return "-1"
    result = []

    for i in common_set:
        x_count = X.count(i)
        y_count = Y.count(i)
        pair_count = min(x_count, y_count)
        result += [i] * pair_count
    result.sort(reverse=True)
    if result[0] == "0": # 결과가 0으로 시작하는 경우
        return "0"
    
    return "".join(result)

print(solution(	"100", "123450"))