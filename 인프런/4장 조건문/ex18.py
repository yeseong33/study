# 주사위 눈을 랜덤으로 발생시켜서 해당하는 숫자를 출력하는 프로그램을 만들기
# randint() 함수를 검색해 사용법을 익힌 후 프로그램을 작성하시오

from random import *
# rnadint(a, b) 함수는 a부터 b까지의 사이에 있는 정수를 반환해주는 함수
num = randint(1, 6)
print('주사위 눈 : ', num)
# random() 함수는 0.0부터 1.0미만의 실수를 반환해 주는 함수
num1 = random()
print(num1)
# randrange(start, stop, step) 함수는 start 에서 stop 까지 step 의 값에 따라 임의의
# 수를 반환 해주는 함수
num = randrange(0, 101, 2)
print(num)
# randrange(a) 함수는 0에서부터 a 미만까지의 임의의 정수값을 반환하는 함수
num = randrange(10)
print(num)

num = randint(1, 6)
print('주사위 눈 : ', num)

if num == 1:
    print('주사위 눈 : ', num)
elif num == 2:
    print('주사위 눈 : ', num)
elif num == 3:
    print('주사위 눈 : ', num)
elif num == 4:
    print('주사위 눈 : ', num)
elif num == 5:
    print('주사위 눈 : ', num)
elif num == 6:
    print('주사위 눈 : ', num)