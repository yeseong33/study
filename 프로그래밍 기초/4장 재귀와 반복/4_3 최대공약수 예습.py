# def gcd(m, n):
#     if n != 0:
#         return gcd(n, m % n)
#     else:
#         return m
#
#
# def gcd(m, n):
#     def loop(m,n,prod):
#         if n != 0:
#             return loop(n,m%n)
#         else:
#             return m
#     return gcd(m,n)

# 내 코드
# def gcd(m, n):
#     while n != 0:
#         t = m
#         m = n
#         n = t % n
#     return m
# # Test code
# print(gcd(48,18))   # 6
# print(gcd(18,48))   # 6
# print(gcd(192,72))  # 24
# print(gcd(18,57))   # 3
# print(gcd(0,11))    # 11
# print(gcd(0,0))     # 0


# 답
# def gcd(m,n):
#     while n != 0:
#         m, n = n, m % n
#     return m
# print(gcd(48,18))   # 6
# print(gcd(18,48))   # 6
# print(gcd(192,72))  # 24
# print(gcd(18,57))   # 3
# print(gcd(0,11))    # 11
# print(gcd(0,0))     # 0

# 실습 4.3 나눠풀기 알고리즘 꼬리재귀 버전

def even(t):
    return t % 2 == 0

def odd(t):
    return t % 2 == 1

#
# def gcd(m,n):
#     def loop(m,n,k):
#         if not (m == 0 or n == 0):
#             if m % 2 == 0 and n % 2 == 0:
#                 return loop(m//2,n//2,2*k)
#             elif m % 2 == 0 and n % 2 == 1:
#                 return loop(m//2,n,k)
#             elif m % 2 == 1 and n % 2 == 0:
#                 return loop(m,n//2,k)
#             elif m <= n:
#                 return loop(m,(n-m)//2,k)
#             else:
#                 return loop(n,(m-n)//2,k)
#         else:
#             if m == 0:
#                 return n*k
#             else: # n == 0
#                 return m*k
#     return loop(m,n,1)
# print(gcd(18,48))

def gcd(m, n):
    k = 1
    while not (m == 0 or n == 0):
        if m % 2 == 0 and n % 2 ==0:
            m, n, k = m//2, n//2, k*2
        elif m % 2 ==0 and n % 2 == 1:
            m = m // 2
        elif m % 2 == 1 and n % 2 == 0:
            n = n // 2
        elif m <= n:
            n = (n-m) // 2
        elif m > n:
            m, n = n, (m-n)//2
    if m == 0:
        return n * k
    else:
        return m * k

print(gcd(18,48))