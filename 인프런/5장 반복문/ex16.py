# 플래그 변수를 사용한 무한 루프 문제
# 1. 증속 2. 감속 3. 중지 를 출력하고 사용자의 입력을 받아
# 증속이면 속도를 10증가 하고 출력
# 감속이면 속도를 10감소 하고 출력
# 중지이면 플래그 변수를 이용해 무한루프를 빠져나간다.


print('1. 증속 2. 감속 3. 중지')
a = 0
s = 0
run = True
while run:
    a = int(input())
    if a == 3:
        print('현재 속도는', s,'입니다.')
        run = False
    elif a == 1:
        s += 10
    else:
        s -= 10


# run = True
# speed = 0
# keyCode = 0
#
# while run:
#     print('------------------------')
#     print('1. 증속 | 2. 감속 | 3. 중지')
#     keyCode = input('선택 : ')
#     if int(keyCode) == 1:
#         speed += 10
#         print('현재 속도 : ', speed)
#     elif int(keyCode) == 2:
#         if speed <= 0:
#             speed = 0
#         else:
#             speed -= 10
#         print('현재 속도 : ', speed)
#     # 중지일 경우 플래그 변수를 False 로 변환해 무한루프를 빠져나온다.
#     elif int(keyCode) == 3:
#         run = False
#     # 사용자가 잘못 입력했을 경우
#     else:
#         print('잘못된 입력값입니다.')
# print('프로그램 종료')