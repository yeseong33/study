# 임의의 숫자를 발생시켜 숫자를 맞추는 게임을 만들어보기

from random import *

cnt = 0
num = randint(1, 100)
ans = 0
print('1~100 사이의 숫자를 맞춰보세요.')
while num != ans:
    ans = int(input('숫자를 입력하세요. : '))
    if num > ans:
        print('틀렸습니다!, 더 큰 수입니다.')
    else:
        print('틀렸습니다!, 더 작은 수입니다.')
    cnt += 1
print('%d 정답입니다. %d회 만에 맞추셨습니다!' % (num, cnt))

