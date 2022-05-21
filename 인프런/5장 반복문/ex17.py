# 중첩 루프(nested loop, 더블루프)
# 반복문 안에 또 다른 반복문이 들어가 있는 형태
# * 로 사각형 만들기

for y in range(5):
    for x in range(5):
        if y == 0 or y == 4:
            print('*', end = ' ')
        elif x == 0 or x == 4:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print('')
