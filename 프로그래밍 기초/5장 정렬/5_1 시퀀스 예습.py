# 리스트(List)

# ns = [3, 5, 4, 2]
# ['컴퓨터과학', '대학교', '소프트웨어', '인공지능']

# 정렬
# ns.sort()
# ns.sort(reverse =  True)

# 시퀀스
# 시퀀스 타입:
# 리스트 list = [4, 6, 9, 11] -> 수정 가능
# 튜플 Tuple = ('컴퓨터과학', 1, '짱'0
# 정수범위 range = range(3, 9)

# for 루프
#
# for i in [1, 4, 5, 7]:
#     print(i,'월')
#
# for x in ('고록', '고록2'):
#     print(x,'고')


from time import sleep


def countdown(n):
    while n > 0:
        print(n)
        sleep(1)
        n -= 1
    print("Launch!")


def countdown(n):
    for i in range(n, 0, -1):
        print(i)
        sleep(1)
    print('Launch!')


def sigma(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


print(sigma(10))


def sumrange(m, n ):
    sum = 0
    for i in range(m, n+1):
        sum += i
    return sum


print(sumrange(4, 7)) # 22
print(sumrange(2, 8)) # 35


def fac(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans


print(fac(3)) # 6
print(fac(4)) # 24
print(fac(6)) # 720


def power(b, n):
    prod = 1
    for i in range(n):
        prod = b * prod
    return prod


print(power(2,2)) # 4
print(power(2,4)) # 16
print(power(3,2)) # 9
print(power(4,2)) # 16
print(power(5,3)) # 125


def power(b, n):
    prod = 1
    while n > 0:
        prod = b * prod
        n -= 1
    return prod


print(power(2,5)) # 120