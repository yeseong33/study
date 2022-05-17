# def BMI(h, w):
#     bmi = w / h**2
#     if bmi < 18.5:
#         print('저체중입니다.')
#     elif 18.5<= bmi < 22.9:
#         print('정상입니다.')
#     elif 23.0<= bmi < 24.9:
#         print('과체중입니다.')
#     elif 25.0<= bmi < 29.9:
#         print('경도비만입니다.')
#     elif 30<= bmi :
#         print('고도비만입니다.')
#     return bmi
# BMI(1.6, 47)

# import turtle as t
# def n_polygon(n, a):
#     t.Turtle()
#     t.shape('turtle')
#     t.speed(-1)
#     for j in range(10):
#         for i in range(n):
#             t.forward(a)
#             t.left(360/n)
#         t.left(360/n)
#     return t.exitonclick()
#
# n_polygon(5, 100)


# def a(b):
#     if b > 1:
#         return a(b-1) * b
#     else:
#         return 1
#
# print(a(4))


# country_list = ['미국', '일본', '유럽', '중국']
# rate = [1182.5, 1078.14, 1286.74, 169.22]
# def exchange():
#     if c in country_list:
#         m_code = country_list.index(c)
#     else:
#         print('해당 국가 정보가 없습니다.')
#
#     result = round(m / rate[m_code], 2)


    # if c == '미국':
    #     ex = kw / 1182.5
    #     return ex
    # elif c == '일본':
    #     ex = kw / 1078.14
    #     return ex
    # elif c == '유럽':
    #     ex = kw / 1286.74
    #     return ex
    # elif c == '중국':
    #     ex = kw / 169.22
    #     return ex
    # else:
    #     print('해당 국가 정보가 없습니다.')


# kw = int(input('환전 금액(원)을 입력하세요: '))
# c = input('국가를 입력하세요: ')
# print(exchange())


# def electricity(kwh):
#     if kwh > 0:
#         if kwh <= 200:
#             return 100 * kwh
#         elif 200 < kwh <= 300:
#             return electricity(200) + 200 * (kwh%200)
#         else:
#             return electricity(300) + 300 * (kwh%300)
#     else:
#         return 0
#
#
# print(electricity(150))
# print(electricity(250))
# print(electricity(350))
