# 직각삼각형 판별하기
# a = int(input('변 a의 길이를 입력하세요'))
# b = int(input('변 b의 길이를 입력하세요'))
# c = int(input('변 c의 길이를 입력하세요'))
#
# if c < a+b:
#     if a**2 + b**2 == c**2:
#         print('직각삼각형입니다.')
#     else:
#         print('직각삼각형이 아닙니다.')
# else:
#     print('삼각형이 아닙니다.')

# 정수의 종류를 판벼하는 스마트 터틀
# import turtle
#
#
# t = turtle.Turtle()
# t.shape('turtle')
#
# t.penup()
# t.goto(100,100)
# t.write('입력된 정수는 양의 정수입니다.')
# t.goto(100,-100)
# t.write('입력된 정수는 음의 정수입니다.')
# t.goto(100,0)
# t.write('입력된 정수는 0입니다.')
#
# t.goto(0,0)
# t.pendown()
#
# s = turtle.textinput('','숫자를 입력하세요:')
# e = int(s)
#
#
# if e > 0:
#     t.goto(100,100)
# if e == 0:
#     t.goto(100,0)
# if e < 0:
#     t.goto(100,-100)


# print('주민등록번호의 성별 정보 번호를 생성합니다.')
#
# id_num = int(input('생성번호 : '))
#
# if id_num == 1 or 3:
#     print('남성입니다.')
# elif id_num == 2 or 4:
#     print('여성입니다.')
#
# print('프로그램을 종료합니다.')

# a = input('1번 전지가 있습니까?(Y/N) : ')
# b = input('2번 전지가 있습니까?(Y/N) : ')
# o = '전구에 불이 꺼집니다.'
# f = '전구에 불이 켜집니다.'
#
# if a == y and b == y:
#     return o
# if a == y or b == c:
#     return o
# if a == n and b == n:
#     return f
#
# print('직렬연결'+o)


# if a == 'Y' and b == 'Y':
#     print('직렬연결')
# else:
#     print('불이 꺼져있음')
#
# if a.upper() == 'Y' and b.upper() == 'Y':
#     print('병렬연결')
# else:
#     print('불이 꺼져있음')


# y = int(input('년도를 입력하세요. : '))
#
# if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#     print(str(y)+'년도는 윤년입니다.')
# else:
#     print(str(y)+'년도는 윤년이 아닙니다.')




# import turtle
#
# t = turtle.Turtle()
# t.shape('turtle')
# e = turtle.textinput('','도형을 입력하세요.')
#
# if e == '직사각형':
#     r1 = int(turtle.textinput('','가로의 길이를 입력하세요.'))
#     r2 = int(turtle.textinput('','세로의 길이를 입력하세요.'))
#     for i in range(2):
#         t.forward(r1)
#         t.left(90)
#         t.forward(r2)
#         t.left(90)
# elif e == '정삼각형':
#     r = int(turtle.textinput('', '한변의 길이를 입력하세요.'))
#     for i in range(3):
#         t.forward(r)
#         t.left(120)
#
# elif e == '원':
#     r = int(turtle.textinput('', '반지름의 길이를 입력하세요.'))
#     t.circle(r)
#
# turtle.exitonclick()





