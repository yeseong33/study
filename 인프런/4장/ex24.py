# 수자 추측 게임 만들기
# 1 ~ 100

from random import *
# 1~100까지 임의의 수를 발생시키는 코드
rand_num = randint(1,100)
print('발생한 난수 : ',rand_num)
user_num = int(input('숫자를 맞춰보세요. (1~100) : '))
n = 1

while True:
    if user_num == rand_num:
        print('정답입니다.',n,'번만에 맞췄습니다. 게임을 종료합니다.')
        break
    elif user_num > rand_num:
        print('입력한 숫자가 큽니다.')
        print('시도 횟수 : ',n)
    else:
        print('입력한 숫자가 작습니다.')
        print('시도 횟수 : ', n)
    user_num = int(input('다시 입력해 주세요. : '))
    n += 1