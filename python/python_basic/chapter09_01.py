#Chapter09-1
#파일 읽기 및 쓰기

#읽기 모드: r, 쓰기모드: w, 추가모드: a, 텍스트모드: t, 바이너리 모드:b
#상대 경로('../,./'), 절대 경로 ('C:\Django\example..')

#파일 읽기(Read)
#예제1

f= open('./resource/it_news.txt', 'r', encoding='UTF-8') #t는 디폴트임으로 r= rt
#속성 확인
print(dir(f))
#인코딩 확인
print(f.encoding)
#파일 이름
print(f.name)
#모드 확인
print(f.mode)
cts = f.read() # 글자 그래도 불러오는 함수
print(cts)
#반드시 close
f.close()

#예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c=f.read()
    print(c)
    print(iter(c))
    print(list(c))
print()

#예제3
#read() : 전체읽기, read(10) : 10Byte 영문은 10글자 정도 한글은 2~3바이트
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c=f.read(20)
    print(c)
    c=f.read(20)     #내가 어디까지 읽었는지 내부적으로 파이썬은 기억 하고 있음.
    print(c)
    f.seek(0,0) # 맨처음으로 회귀
    c=f.read(20)
print()

#예제4
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
print()

#예제5
#readLines: 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts= f.readlines()
    print(cts)
    print()
    for c in cts:  #원상 복구
        print(c, end='')
print()

#파일 쓰기(write)
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python1\n')

#예제2
with open('./resource/contents1.txt', 'at') as f:
    f.write('I love python2\n')

#예제3
#writelines: 리스트 -> 파일
with open('./resource/contents1.txt', 'w') as f:
    list= ['Orange\n','Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

#예제4
with open('./resource/contents1.txt', 'w') as f:
    print('Test Text Write', file= f)
    print('Test Text Write', file= f)
    print('Test Text Write', file= f)



