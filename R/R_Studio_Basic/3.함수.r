#기본 함수 base, stats, utils 등

print(123)
print('asdf')

round(12.345)
round(12.345,1) # 소수첨 첫째 자리 반올림
round(x = 3.14125, digits = 2)

floor(12.9) #내림

#사용자 정의 함수
aaa = function(x){}
aaa(x=2) #함수에 아무 값이 없어서 NULL값 출력
#예제1
bbb= function(){
    print('출력 완료')
}
bbb()
#예제2
ccc = function(x= 20){
    x+3
}
ccc()  #저런식으로 인자값이 정해진 상태에서는 자동으로 인자값이 들어감
ccc(3)  #인자값을 지정해주면 지정해준 값으로 들어감

ddd= function(aa, bb){
    numbers = aa + bb
    return(numbers)
}
ddd(156, 10)

#문제 1 두숫자를 입력받아서 곱한 다음 100을 뺸 값을 출력으로 하는 사용자 정의 함수를 생성하시오.

fff= function(x, y){
    result = x*y -100
    return(result)
}
fff(5, 10)
