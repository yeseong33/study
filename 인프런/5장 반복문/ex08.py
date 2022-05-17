# 사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램을 만들기

n = int(input('단을 입력하세요 : '))
for i in range(1,10):
    if n < 2 or n > 9:
        print('2~9 범위 내의 단을 입력하세요.')
        break
    print(n, '*', i, '= ', n*i)
    print('{0} * {1} = '.format(n, i), n*i)