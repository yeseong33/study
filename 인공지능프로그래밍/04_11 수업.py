# sum1 = 0
# for i in range(1, 101):
#     sum1 += i
# print('1부터 100 까지의 합은', sum1, '입니다.')


# num = int(input('정수를 입력하세요. : '))
# fact = 1
#
# for i in range(1, num+1):
#     fact *= i
# print(i,'!은 ', fact, '이다.', sep = '')


# cout = 1
# sum1 = 0
# while cout <= 100:
#     sum1 += cout
#     cout += 1
# print('1부터 100까지의 합은', sum1, '입니다.')


# passWord = ""
# while passWord != '0923':
#     passWord = input('패스워드를 입력하세요.')
# print('로그인')


# from random import *
# R_num = randint(1,100)
# anser = 0
# count = 0
# while anser != R_num:
#     anser = int(input('숫자를 입력하세요 : '))
#     if anser > R_num:
#         print('큽니다.')
#     elif anser < R_num :
#         print('작습니다.')
#     count += 1
# print('맞췄습니다. 시도 횟수 :', count)


# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(100000)
# for i in range(6):
#     t.circle(100)
#     t.left(60)
# turtle.exitonclick()


# print('A')
# print('B')
# for i in range(2):
#     print('C D')


# import turtle as t
# t.shape('turtle')
# num = int(t.textinput('몇각형을 원하시나요?', ''))
# angle = 180 * (num-2) // num
#
# for i in range(num):
#     t.forward(100)
#     t.left(180-angle)
# t.exitonclick()


# import turtle
# from random import *
# t = turtle
# t.shape('turtle')
# t.speed(1000000000)
# R1 = randint(1, 100)
#
# for i in range(R1):
#     R2 = randrange(1, 100)
#     t.forward(R2)
#     t.left(randint(-180, 180))
# t.exitonclick()


from random import *
point = 50

while True:
    room = randint(1, 3)
    ans = int(input('방 번호를 입력하세요. : '))
    if room != ans:
        point -= 10
        print('방이 비어있습니다. 현재포인트 :', point)
    else:
        point += 100
        print('범인을 찾았습니다. 게임을 종료합니다. 현재포인트 :', point)
        break


# for i in range(3,9,2):
#     print(i)


# sum = 0
# # for i in range(1,11):
# #     sum += i
# # print('합계', sum)


# import time
# for i in range(1,11):
#     print(11-i)
#     time.sleep(1)
# print('Fire!')

