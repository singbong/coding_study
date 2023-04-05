"""
문자열 재정렬

알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을
오름 차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.


"""
data= input()
answer= []                  #문자 담을 리스트 생성
number=0                    #숫자들을 합친 값 저장
for i in data:              #문자열 인덱스 대입
    if 65<= ord(i) and ord(i) <= 95:  #아스키 코드고 65부터 95까지 A~Z
        answer.append(i)        #문자 리스트에 문자 추가
    else:
        number+= int(i)         #숫자들을 더한 값 number에 업데이팅
answer.sort()                   #문자 오름차순 정렬
if number != 0:
    answer.append(str(number))  #마지막으로 숫자 추가
result= ''.join(answer)         #리스트를 문자열로 바꿔주는 함수 실행
print(result)                   #답 출력

