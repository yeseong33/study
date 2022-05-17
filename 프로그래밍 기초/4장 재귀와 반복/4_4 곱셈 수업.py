def mult(m,n):
    def loop(m,n,k):
        if n > 0:
            return loop(m, n-1, k+m)
        else:
            return k
    return loop(m, n, 0)


print(mult(7, 7))


def mult(m, n):
    k = 0
    while n > 0:
        n -= 1
        k += m
    return k


print(mult(7, 7))


def mult(m, n):
    if n >0:
        if n % 2 == 0:
            return mult(m+m, n / 2)
        elif n % 2 == 1:
            return m + mult(m, n - 1)
    else:
        return 0
print(mult(7, 7))


def mult(m, n):
    def loop(m, n, k):
        if n > 0:
            if n % 2 == 0:
                return loop(2*m, n/2, k)
            elif n % 2 == 1:
                return loop(m, n-1, k+m)
        else:
            return k
    return loop(m, n, 0)

print(mult(7, 7))


def mult(m, n):
    k = 0
    while n > 0:
        if n % 2 == 0:
            m, n = m+m, n/2
        else:
            n, k = n-1, k+m
    return k


print(mult(7, 7))


def R(m, n):
    if n > 0:
        if n % 2 == 1:
            return R(2*m, n//2)+m
        else:
            return R(2 * m, n//2)
    else:
        return 0


print(R(57, 86))


def R(m, n):
    def loop(m, n, k):
        if n > 0:
            if n % 2 == 1:
                return loop(m+m, n//2, k+m)
            else:
                return loop(m+m, n//2, k)
        else:
            return k
    return loop(m, n, 0)


print(R(57, 86))


def R(m, n):
    k = 0
    while n > 0:
        if n % 2 == 1:
            m, n, k = m+m, n//2, k+m
        else:
            m, n, k = m + m, n // 2, k
    return k


print(R(57, 86))





