# 2주차
# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
#
# turtle.exitonclick()

# print('시간순삭 파이썬')
# print('9*8은 72입니다.')

# print('너무','반짝'*2, '눈이 부셔', 'No '*5)
# print('너무', '깜짝'*2, '놀란 나는', 'Oh '*5)
# print('너무', '짜릿'*2, '몸이 떨려', 'Gee '*5)

# import turtle
# t = turtle.Turtle()
# t.shape('turtle') # 'square'
# t.width(10) # 팬 두께
# t.color('blue') # 팬 색깔
# t.circle(100) # 반지름이 100인 원을 그림

# t.down
# t.up
# t.goto(x,y)


# import turtle
# R = int(input('원의 반지름을 입력하시오: '))
# Colar = input('원의 색깔을 입력하시오: ')
# t = turtle.Turtle()
# t.shape('turtle')
# t.color(Colar)
# t.begin_fill()
# t.circle(R)
# t.end_fill()
# turtle.exitonclick()

# 거 = 속 시
# t = int(input('측정 시간(초) 입력: '))
# R = 340 * t
# print('자신의 위치에서 번개가 친 장소까지의 거리=', R, 'm')

# 3주차

# = 는 우변의 값이 좌변에 저장된다는 특별함을 가지고 있다.
# 변수 자신의 값을 갱신할 수 있다.

# 연산자 우선순위
# 하나의 수식에 있는 여러 연산 중 어떤 연산을 먼저 수행할지를 결정

# 화씨온도 - 섭씨온도
# f = int(input('화씨온도: '))
# c = (f - 32) * (5/9)
# print('섭씨온도: ', c)

# import time
# t = time
# G = t.time()
# H = int((G // 60 // 60 + 9) % 24)
# S = int(G % 60)
# M = int(G // 60 % 60)
# print('현재 한국 시간:', H, '시', M, '분', S, '초')

# 4주차

# 자료의 종류
# 정수(int), 실수(float), 문자열(str)

# 거북이와 인사하는 프로그램
# import turtle
# t = turtle.Turtle()
# # t.Turtle()
# t.shape('turtle')
# name = turtle.textinput('','이름을 입력하시오:')
# for i in range(4):
#     t.forward(100)
#     t.left(90)
# t.write('안녕하세요?' + name + '씨, 터틀 인사드립니다.')
# turtle.exitonclick()

# 암호프로그램 만들기
# I = input('평문: ')
# S = I[::-1]
# print('암호문:', S)

# 5주차
# 조건을 따짐
# 조건을 따져서 서로 다른 동작을 하도록 하는 것
# 질문한 후 결정하는 형태를 만들어 준다.

# 순차구조(sequence): 명령어들이 순차적으로 실행되는 구조
# 선택구조(selection): 둘 중의 하나의 명령을 선택하여 실행되는 구조
# 반복구조(iteration): 동일한 명령이 반복되면서 실행되는 구조

# a = int(input('변 a의 길이: '))
# b = int(input('변 b의 길이: '))
# c = int(input('변 c의 길이: '))
# if c < a + b:
#     if c ** 2 == a **2 + b **2:
#         print('직각삼각형입니다.')
#     else:
#         print('직각삼각형이 아닙니다.')

# import turtle
# t = turtle.Turtle()
# a = int(turtle.textinput('','숫자를 입력하시오:'))
# t.shape('turtle')
# t.penup()
# t.goto(100,100)
# t.pendown()
# t.write('입력된 정수는 양의 정수입니다.')
# t.penup()
# t.goto(100,0)
# t.pendown()
# t.write('입력된 정수는 0입니다.')
# t.penup()
# t.goto(100,-100)
# t.pendown()
# t.write('입력된 정수는 음의 정수입니다.')
# t.penup()
# t.home()
# t.pendown()
# if a > 0:
#     t.goto(100,100)
# elif a == 0:
#     t.goto(100, 0)
# else:
#     t.goto(100,-100)
# turtle.exitonclick()

# import random
# print('주민등록번호의 성별 정보 번호를 생성합니다.')
# num = random.randint(1, 2)
# print('생성번호:', num)
# if num == 1:
#     print('남성입니다.')
#     print('프로그램을 종료합니다.')
# else:
#     print('여성입니다.')
#     print('프로그램을 종료합니다.')

# a = input('1번 전지가 있습니까? (Y/N) ')
# b = input('2번 전지가 있습니까? (Y/N) ')
# if (a and b) == 'y':
#     print('직렬연결: 전구에 불이 꺼지지 않습니다.')
#     print('병렬연결: 전구에 불이 꺼지지 않습니다.')
# elif a != b:
#     print('직렬연결: 전구에 불이 꺼집니다.')
#     print('병렬연결: 전구에 불이 꺼지지 않습니다.')
# else:
#     print('직렬연결: 전구에 불이 꺼집니다.')
#     print('병렬연결: 전구에 불이 꺼집니다.')


# 윤년판단
# year = int(input('연도를 입력하세요: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(year,'년은 윤년입니다.')
# else:
#     print(year, '년은 평년입니다.')


# 사용자가 원하는 도형 그리기
# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# Shape = turtle.textinput('도형', '도형을 입력하세요.')
# if Shape == '직각사각형':
#     h = turtle.numinput('가로','가로')
#     l = turtle.numinput('세로','세로')
#     for i in range(2):
#         t.forward(h)
#         t.left(90)
#         t.forward(l)
#         t.left(90)
# elif Shape == '원':
#     r = turtle.numinput('반지름','반지름')
#     t.circle(r)
# else:
#     a = turtle.numinput('길이','길이')
#     for i in range(3):
#         t.forward(a)
#         t.left(120)
# turtle.exitonclick()


# 6주차
# 루프: 동일한 작업을 여러번 수행할 때
# for 루프: 반복횟수를 알 때
# while 루프: 반복횟수는 모르지만, 반복 조건은 알 때

# n각형 그리기
# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# a = int(turtle.textinput('','몇각형을 원하세요?:'))
# ang = 360 // a
# for i in range(a):
#     t.forward(100)
#     t.left(ang)
# turtle.exitonclick()


# 랜덤워크 시뮬레이션
# import turtle, random
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(10000000)
# n = random.randint(1,20)
# for i in range(n):
#     ang = random.randrange(1,360)
#     t.setheading(ang)
#     f = random.randrange(1,100)
#     t.forward(f)
# turtle.exitonclick()


# for i in range(3,9,2):
#     print(i)

# sum =0
# for i in range(1,11):
#     sum += i
# print(sum)

# 7주차

# for i in range(3):
#     for j in range(3):
#         print('* ' , end='')
#     print('')

# 구구단
# for i in range(2,10):
#     for j in range(1,10):
#         print('{:3d}'.format(i * j), end='\t')
#     print()


# 삼각형 만들기
# for i in range(1,5):
#     print('\t' * (4-i), end='')
#     print('*\t' * (2*i-1), end='')
#     print('')
#
#
# for i in range(1,5):
#     print('\t' * (4-i), '*\t' * (2*i-1), sep = '')
#     print('')

# for i in range(1,7):
#     for j in range(1,7):
#         if i + j == 6:
#             print(f'첫번째 주사위= {i} 두번째 주사위= {j}')
