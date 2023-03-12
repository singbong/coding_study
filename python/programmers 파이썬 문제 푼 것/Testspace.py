ar= [1,2,3,4,5]
try:
    ar[2] = 10
        
except Exception:
    print('에러 발생')
else:
    ar.append('엥')

print(ar)