# 파이썬에서의 자료형(Data-type)

#int형을 출력함
print(type(17))
#float형을 출력함
print(type(10.77778))
# str 형을 출력함
print(type('안녕하세요.'))


# 반지름이 r인 구의 부피는 4/3 * pi * r ** 3
# 반지름이 5인 구의 부피를 계산하는 프로그램
r = 5.0
from math import *
volume = 4.0/3.0 * pi * pow(r,3)
print('구의 부피 '+str((volume)))
print(pi)

# 함수만들기
# def volume(r):
#    from math import *
#    return 4.0/3.0 * pi * pow(r,3)
# print(volume(r))


# 구의 겉넓이의 공식 : 4 * pi * pow(r,2)
r = 5
outer_area = 4 * pi * pow(r,2)

