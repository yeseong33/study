# 팩토리얼
# 꼬리재귀
def fac(n):
    def loop(n, k):
        if n > 0:
            return loop(n-1, k * n)
        else:
            return k
    return loop(n, 1)


# while 루프
def fac(n):
    k = 1
    while n > 0:
        k *= n
        n -= 1
    return k


# 삼각수
# 재귀
def trinum(n):
    if n > 0:
        return n + trinum(n-1)
    else:
        return 0


# 꼬리재귀
def trinum(n):
    def loop(n, k):
        if n > 0:
            return loop(n-1, k+n)
        else:
            return k
    return loop(n, 0)


# while 루프
def trinum(n):
    k = 0
    while n > 0:
        n, k = n-1, k+n
    return k


# 덧셈만 가지고 제곱 계산하기
# 재귀
def square(n):
    if n > 0:
        return (n+n-1) + square(n-1)
    elif n < 0:
        return abs(n)+abs(n)-1 + square(n+1)
    else:
        return 0


# Test code
print(square(0))  # 0
print(square(1))  # 1
print(square(-2)) # 4
print(square(3))  # 9
print(square(-4)) # 16
print(square(5))  # 25
print(square(11))
print(square(-11))
print(square(12))
print(square(-12))
print(square(0))


# 꼬리재귀
def square(n):
    def loop(n, k):
        if n > 0:
            return loop(n-1, k+(n+n-1))
        elif n < 0:
            return loop(n+1, k+(abs(n)+abs(n)-1))
        else:
            return k
    return loop(n, 0)


# Test code
print(square(0))  # 0
print(square(1))  # 1
print(square(-2)) # 4
print(square(3))  # 9
print(square(-4)) # 16
print(square(5))  # 25
print(square(11))
print(square(-11))
print(square(12))
print(square(-12))
print(square(0))


# while 루프
def square(n):
    k = 0
    while n != 0:
        if n > 0:
            n, k = n-1, k+n+n-1
        else:
            n, k = n+1, k+abs(n)+abs(n)-1
    return k


# Test code
print(square(0))  # 0
print(square(1))  # 1
print(square(-2)) # 4
print(square(3))  # 9
print(square(-4)) # 16
print(square(5))  # 25
print(square(11))
print(square(-11))
print(square(12))
print(square(-12))
print(square(0))



