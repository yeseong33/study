# 꼬리재귀
def fac(n):
    def loop(n, k):
        if n > 0:
            return loop(n-1, k * n)
        else:
            return k
    return loop(n, 1)


print(fac(1))
print(fac(2))
print(fac(3))
print(fac(4))
print(fac(5))


# while 루프
def fac(n):
    k = 1
    while n > 0:
        k *= n
        n -= 1
    return k


print(fac(1))
print(fac(2))
print(fac(3))
print(fac(4))
print(fac(5))


# 삼각수
# 재귀
def trinum(n):
    if n > 0:
        return n + trinum(n-1)
    else:
        return 0


print(trinum(0))
print(trinum(1))
print(trinum(2))
print(trinum(3))
print(trinum(4))


# 꼬리재귀
def trinum(n):
    def loop(n, k):
        if n > 0:
            return loop(n-1, k+n)
        else:
            return k
    return loop(n, 0)


print(trinum(0))
print(trinum(1))
print(trinum(2))
print(trinum(3))
print(trinum(4))


# while 루프
def trinum(n):
    k = 0
    while n > 0:
        n, k = n-1, k+n
    return k


print(trinum(0))
print(trinum(1))
print(trinum(2))
print(trinum(3))
print(trinum(4))


# 재귀
def square(n):
    # n = abs(n) # 재귀를 할때마다 함수를 호출한다.
    if n > 0:
        return square(n-1) + (n+n -1)
    elif n < 0:
        return square(n+1) + (abs(n)+abs(n)-1)
    else:
        return 0

print(square(0))
print(square(1))
print(square(2))
print(square(3))
print(square(4))
print(square(5))
print(square(11))
print(square(-11))
print(square(12))
print(square(-12))


# 꼬리재귀
def square(n):
    def loop(n, k):
        if n > 0:
            return loop(n-1, k+n+n-1)
        # elif n < 0:
        #     return loop(n+1, k+abs(n)+abs(n)-1)
        else:
            return k
    return loop(abs(n), 0)


print(square(11))
print(square(-11))
print(square(12))
print(square(-12))


# while 루프
def square(n):
    k = 0
    n = abs(n) # 한번만 사용 되므로 이곳에 쓰여도 적절하다.
    while n != 0:
        if n > 0:
            n, k = n-1, k+n+n-1
        # elif n < 0:
        #     n, k = n+1, k+abs(n)+abs(n)-1
    return k


print(square(11))
print(square(-11))
print(square(12))
print(square(-12))


# 항상 square(n)의 답이 항상 n^2가 되는지 증명하세요

# 기초단계:
# n = 0
# square(0) == 0^2

# 귀납단계:
# n != 0
# k < n 인 임의의 k에 대해서,
# square(k) == k^2 이라 가정하자.

# square(k+1) == (k+1)^2 임을 증명
# square(k+1) == square(k) + (k+1+k+1 -1)
#             == k^2 + k + k +1
#             == k*k + 2 *k +1
#             == (k+1)^2




