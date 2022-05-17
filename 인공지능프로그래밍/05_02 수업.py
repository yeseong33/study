# 스파이럴 그리기
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# colar_1 = ['red', 'purple', 'blue', 'green', 'yellow','orange']
# n = 5
# k = 1
# t.speed(0)
# while n < 500:
#     K = k % 6
#     t.color(colar_1[K])
#     t.forward(n)
#     t.left(91)
#     n += 5
#     k += 1
# turtle.exitonclick()


# 실습 습도 구하기
# list = [4.8, 9.4, 17.3, 30.4]
# nv = float(input('현재 수증기량 입력: '))
# k = float(input('현재 온도 입력: '))
# n = int(k//10)
# ov = list[n]
# v = nv / ov * 100
# print('현재 습도는', v, '% 입니다.')
# print('프로그램을 종료합니다.')


# 리스트 함축 사용
# list = [i for i in range(0,100) if i % 2 == 0 and i % 3 ==0]
# print(list)

# 누적값 리스트 만들기
# list_o = [10, 20, 30, 40, 50]
# list_n = [sum(list_o[0:i+1]) for i in range(len(list_o))]
# print(list_n)

