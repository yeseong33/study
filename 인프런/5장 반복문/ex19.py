# 중첩 루프를 이용해 아래와 같이 출력하는 프로그램 작성
# 출력
#     *
#    ***
#   *****
#  *******

# (1)
for i in range(4):
    print(' ' * (3-i), end = '')
    print('*' * (2*i+1), end = '')
    print('')

for i in range(4):
    print(' ' * (3-i), end = '')
    for j in range(2*i+1):
        print('*', end = '')
    print('')


# (2)
for i in range(5):
    # 중앙 정렬 ^ 기호 사용
    print('{:^9}'.format("*"*(2*i+1)))


# 출력
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

# 내 코드
for i in range(10):
    if i <= 4:
        print(' '*(4-i), end = '')
        for j in range(2*i+1):
            print('*', end = '')
    else:
        print(' '*(i-5), end='')
        for j in range(19-i*2):
            print('*', end='')
    print('')


# 풀이
for i in range(1, 6):
    for j in range(5-i):
        print(' ', end = '')
    for j in range(1, i*2):
        print('*', end = '')
    print('')
for i in range(5):
    for j in range(i):
        print(' ', end = '')
    for j in range(10, 2*i+1, -1):
        print('*', end = '')
    print('')

