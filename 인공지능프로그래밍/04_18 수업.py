# 몬드리안 터틀
# import turtle, random
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(100000000)
# for j in range(100):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     t.color(r, g, b)
#     t.penup()
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     t.goto(x, y)
#     t.pendown()
#     length = random.randint(10, 300)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(length)
#         t.left(90)
#     t.end_fill()
# turtle.exitonclick()

#
# for i in range(3,0):
#     for j in range(i,i+1):
#         print('\t'* i,'*')

# 삼각형 만들기
for i in range(1,5):
    print('\t' * (4-i), '*\t' * (2*i-1), sep = '')
    print('',end = '\n')


# ###### 시험 중첩반복문 자료 7p
# 20 ~ 25 문제
# 시간 50분
# 참, 거짓 관련 코드, 실행 결과(골고루)
# 제어, 반복문 빈칸 채우기
# 각 주차 대표적 용어 정리하기
# 컴퓨터 x


# for i in range(1,5):
#     for j in range(5-i):
#         print('',end = '')
#     for j in range(1, i):
#         print('*', end = '')
#     for i in range(i, 0, -1):
#         print('*', end = '')
#     print(' \n')


# 소수 나타내기
# a = []
# for i in range(2, 21):
#     n = 0
#     for j in range(2, i+1):
#         if i != j and i % j == 0:
#             n += 1
#     if n == 0:
#         # a.append(i)
#         print(i, end=' ')



# for i in range(1,7):
#     for j in range(1,7):
#         if i + j == 6:
#             print('첫번때 주사위 =  ',i,' 두번째 주사위 =  ',j, sep='')

m = int(input('정수 1을 입력하세요'))
n = int(input('정수 2을 입력하세요'))
m = min(m,n)

while m > 0:
    if n > m:
        r = n % m
    else:
        r = m % n
    m, n = n, r