# 전화 번호 저장 및 호출 프로그램
#전화번호 입력, 전화번호 출력, 전화번호 삭제, 전화번호 검색
Person = dict()
num= 0
#메뉴
def Menu():
    print('|{:<46s}|'.format(''))
    print('|{:<40s}|'.format('1.전화번호 입력'))
    print('|{:<38s}|'.format('2.전화번호 전체 출력'))
    print('|{:<40s}|'.format('3.전화번호 검색'))
    print('|{:<40s}|'.format('4.전화번호 삭제'))
    print('|{:<46s}|'.format('5.Exit'))
    num = input('메뉴를 입력 해주시오 : ')
    return num
#전화번호 입력 
def Insert():
    while 1:
        name = input('이름을 입력하시오(나가기는 q): ')
        phone_num = input('핸드폰 번호를 입력하시오 : ')
        if name not in Person.keys():
            if Person.get(name) == [phone_num]:
                print('이미 입력 된 데이터 입니다.')       
            else:
                Person[name] = [phone_num]
                print('데이터 입력 완료')
                break
        if name.strip() == 'q':
            break
        if name in Person.keys():
            if Person.get(name) == [phone_num]:
                print('이미 입력 받은 데이터입니다.')           
            else:
                Person[name].append(phone_num)
                print('동명이인의 데이터 입력 완료')
                break
#전화 번호 전체 출력
def Print():
    if Person:
        for i in Person.keys():
            print('이름: {:<20} / 전화번호: {:<20}'.format(i, ','.join(Person.get(i))))
        print('모든 데이터 출력 완료')
    else:
        print('데이터가 없습니다')       
#','.join() 메소드 설명
"""
.join()은 문자열 메서드 중 하나로, 문자열로 결합하는 역할을 합니다.

','.join(Person.get(i))는 Person 딕셔너리의 i 키에 해당하는 값을 쉼표로 구분된 문자열로 변환하는 것입니다. 
Person.get(i)는 리스트를 반환하므로, ','.join(Person.get(i))는 리스트의 요소를 쉼표로 구분하여 하나의 문자열로 합칩니다.

예를 들어, Person.get(i)가 ['010-1234-5678', '02-123-4567'] 라면, ','.join(Person.get(i))는 '010-1234-5678,02-123-4567'을 반환합니다. 
이 문자열은 '이름: {:<20} / 전화번호: {:<20}'.format(i, Person.get(i))에 포맷팅될 수 있습니다.

"""
#전화 번호 검색
def Search():
    num2 = 0
    if Person:
        search = input("찾을 이름 또는 전화번호를 입력 하시오 : ")
        for i, v in enumerate(list(Person.keys())):
            if search in v or search in str(list(Person.values())[i]):
                print('이름: {:<20} / 전화번호: {:<20}'.format(v, ', '.join(list(Person.values())[i])))
                """
                list(Person.values())[i]의 결과는 Person 딕셔너리에서 i번째 키에 해당하는 값이 됩니다. 만약 그 값이 하나의 문자열인 경우, 
                문자열을 그대로 출력할 수 있습니다. 하지만 만약 그 값이 리스트 형태라면, list(Person.values())[i]는 리스트를 반환하기 때문에 
                문자열로 변환해주어야 합니다. join() 메소드는 리스트의 모든 요소를 하나의 문자열로 결합해주는 메소드이므로, 리스트를 문자열로 
                변환하기 위해 사용하는 것입니다.
                """
                num2= num2 + 1
        if num2 > 0:
            print('데이터 출력 완료')
        if num2 == 0 :
            print('일치하는 정보가 없습니다. ')
    if not Person:
        print('데이터가 없습니다')
#전화번호 삭제
def Delete():
    name= input('삭제 할 사람의 이름을 입력해주세요 : ')
    for i in range(0, len(list(Person.keys()))):
        if name == list(Person.keys())[i]:
            Person.pop(name)
            print('데이터 삭제가 완료되었습니다.')
            break
    else:
        print('존재 하지 않는 이름을 입력하셨습니다.')
#데이터 저장
def dataWrite():
    with open('./전화번호부 프로그램 공부/DB.txt', 'w', encoding="UTF-8") as f:
        for name in list(Person.keys()):
            f.write(f'{name} : {", ".join(list(Person.get(name)))}\n')
            #', '.join 은 list를 str형식으로 바꿔줌
#데이터 불러오기
def dataPrint():
    with open('./전화번호부 프로그램 공부/DB.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            name, phones = line.strip().split(' : ') # :를 기준으로 문자열을 쪼개서 리스트형태로 만들어주고 strip은 문자열의 앞 뒤 공백 없앰
            Person[name] = phones.split(', ')
class MainFunction:
    dataPrint()
    while 1:
        num= 0
        num = Menu() #이렇게 안하면 num값이 Menu함수 안에서만 돌고 끝나서 Menu함수의 리턴 값음 num이라고 선언
        try:
            if int(num) == 1:
                Insert()
            elif int(num) == 2:
                Print()
            elif int(num) == 3:
                Search()
            elif int(num) == 4:
                Delete()
            elif int(num) == 5:
                print('프로그램 종료')
                dataWrite()
                break
            else:
                print('메뉴를 올바르게 입력 해주세요')
        except Exception as f:
            print(f)
            print('메뉴를 다시 선택 하시오')