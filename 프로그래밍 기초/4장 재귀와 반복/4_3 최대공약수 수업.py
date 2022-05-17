# def gcd(m, n):
#     while n != 0:
#         m ,n = n, m % n
#         # 동시지정이 아닐 경우 또 다른 변수가 필요하다.
#     return m
# # # Test code
# print(gcd(48,18))   # 6
# print(gcd(18,48))   # 6
# print(gcd(192,72))  # 24
# print(gcd(18,57))   # 3
# print(gcd(0,11))    # 11
# print(gcd(0,0))     # 0
#
# def gcd(m, n):
#     if not(m == 0 or n == 0):
#         if m % 2 == 0 and n % 2 == 0:
#             return 2*gcd(m/2, n/2)
#         elif m % 2 == 0 and n % 2 == 1:
#             return gcd(m/2, n)
#         elif m % 2 == 1 and n % 2 == 0:
#             return gcd(m, n/2)
#         elif m % 2 == 1 and n % 2 == 1:
#             if m <= n:
#                 return gcd(m,(n-m)/2)
#             else:
#                 return gcd(n,(m-n)/2)
#         elif m == 0:
#             return n
#         else:
#             return m

def gcd(m, n):
    def loop(m, n, k):
        if not (m == 0 or n == 0):
            if m % 2 == 0 and n % 2 == 0:
                return loop(m//2, n//2, 2*k)
            elif m % 2 == 0 and n % 2 == 1:
                return loop(m//2, n, k)
            elif m % 2 == 1 and n % 2 == 0:
                return loop(m, n//2, k)
            elif m % 2 == 1 and n % 2 == 1:
                if m <= n:
                    return loop(m, (n-m) // 2, k)
                else:
                    return loop(n, (m-n) // 2, k)
        else:
            if m == 0:
                return n * k
            else:
                return m * k
    return loop(m, n, 1)


print(gcd(18, 48))

def gcd(m,n):
    k = 1
    while not(m == 0 or n == 0):
        if m % 2 == 0 and n % 2 == 0:
            m, n, k = m//2, n//2, 2*k
        elif m % 2 == 0 and n % 2 == 1:
            m, n = m // 2, n
        elif m % 2 == 1 and n % 2 == 0:
            m, n = m , n//2
        elif m <= n:
            n = n -m
        else:
            m, n = n, (m - n) // 2
    if m == 0:
        return n * k
    else:
        return m * k


print(gcd(18, 48))