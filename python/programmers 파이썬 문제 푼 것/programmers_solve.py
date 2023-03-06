"""
제목: 문자열 내 맘대로 정렬하기

문제 설명
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

제한 조건
strings는 길이 1 이상, 50이하인 배열입니다.
strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
모든 strings의 원소의 길이는 n보다 큽니다.
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

"""
def solution(strings, n):
    answer = dict()
    result= list()
    strings.sort() #인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
    for i in strings:      #n번째 인덱스를 key에 strings 원소를 values에 넣음으로써 중복된 key가 있을 경우 같은 key에 values 추가
        if i[n] in answer.keys():
            answer[i[n]].append(i)
        else:
            answer[i[n]] = [i]
    f= list(answer.keys())   
    f.sort()   #n번째 인덱스가 들어가있는 answer 딕셔너리의 key값들을 오름차순 정렬
    for i in f:                 #정렬된 key값 순서로 value 방출
        p= answer.get(i)
        for k in p:
            result.append(k)

    return result
# print(solution(["abce", "abcd", "cdx"], 2))

##########################################################################################################################################
"""
제목: 숫자 문자열과 영단어

네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 
게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

제한사항
1 ≤ s의 길이 ≤ 50
s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.
"""
def solution(s):
    dic1 = dict(zero= '0', one= '1', two= '2', three= '3', four= '4', five= '5', six= '6', seven= '7', eight= '8', nine= '9')

    for i in list(dic1.keys()):
        if i in s:
            s= s.replace(i, dic1.get(i))
        else:
            continue

    return int(s)
# print(solution("zero4seveneight"))
###########################################################################################################################################
"""
제목: K번째 수

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
array의 길이는 1 이상 100 이하입니다.
array의 각 원소는 1 이상 100 이하입니다.
commands의 길이는 1 이상 50 이하입니다.
commands의 각 원소는 길이가 3입니다.
"""


def solution(array, commands):
    answer = []
    
    for i in commands:
        answer.append(sorted(array[i[0]-1:(i[1])])[i[2]-1])  
    # commands 리스트의 원소를 한개씩 불러와 값 대로 슬라이싱을 한다음 오름차순정렬한 후 해당하는 인덱스를 answer리스트에 저장    
    return answer
# print(solution([1, 5, 2, 6, 3, 7, 4], [[4, 4, 1]]))
##########################################################################################################################################



