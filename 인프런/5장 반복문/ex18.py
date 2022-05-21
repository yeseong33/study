# 중첩 루프를 사용해 아래와 같이 출력하는 프로그램을 작성
# 출력결과
# *
# **
# ***
# ****
# *****

# (1)
for x in range(5):
    for y in range(x+1):
        print('*', end ='')
    print('')

# (2)
# format 함수 이용
print('정수값 : {}, str : {}, float : {}'.format(10, '안녕하세요', 10.1))
print('정수값 : {0}, str : {1}, float : {2}'.format(10, '안녕하세요', 10.1))
print('정수값 : {2}, str : {1}, float : {0}'.format(10, '안녕하세요', 10.1))

# 공간이나 0으로 채울수 있다.
# : 을 기준으로 우측, 좌측 >, < 기호를 사용해 방향을 지정
print("숫자 '{:>05d}'".format(300)) # 오른쪽으로 밀어 출력
print("숫자 '{:<05d}'".format(300)) # 왼쪽으로 밀어 출력


for i in range(1, 6):
    print('{:<5}'.format('*' * i))

# *****
# ****
# ***
# **
# *

# (1)
for i in range(5):
    for j in range(5-i):
        print('*', end = '')
    print('')

# (2)
for i in range(5):
    print('*' * (5-i))