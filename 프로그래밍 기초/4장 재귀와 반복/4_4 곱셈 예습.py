# def mult(m, n):
#     if n > 0:
#         return m + mult(m, n-1)
#     else:
#         return 0
#
# print(mult(9,9))
#
# def mult(m,n):
#     def loop(n,k):
#         if n > 0:
#             return loop(n-1, m + k)
#         else:
#             return k
#     return loop(n,0)
#
# print(mult(9,9))
#
# def mult(m,n):
#     k = 0
#     while n > 0:
#         k += m
#         n -= 1
#     return k
#
# print(mult(9,9))
#
#
# 덧셈, 뺄셈, 절반 알고리즘
# def mult(m, n):
#     if n > 0:
#         if n % 2 == 0:
#             return mult(2*m, n/2)
#         elif n % 2 == 1:
#             return m+mult(m, n-1)
#     else:
#         return 0
#
# print(mult(9,9))
# #
# def mult(m,n):
#     def loop(m,n,k):
#         if n > 0:
#             if n % 2 == 0:
#                 return loop(2*m, n/2,k)
#             elif n % 2 == 1:
#                 return loop(m, n-1, k+m)
#         else:
#             return k
#     return loop(m, n, 0)
#
# print(mult(9,9))
#
# def mult(m,n):
#     k = 0
#     while n > 0:
#         if n % 2 == 0:
#             m, n = 2*m, n/2
#         elif n % 2 == 1:
#             k, n= k+m, n-1
#     return k
# print(mult(9,9))



# 러시아 농부 알고리즘

#재귀
def R(m, n):
    if n > 0:
        if n % 2 == 1:
            return m + R(2*m, n//2)
        elif n % 2 == 0:
            return R(2*m, n//2)
    else:
        return 0

print(R(57,86))


# 꼬리재귀
def R(m,n):
    def loop(m, n, k):
        if n > 0:
        # 종료조건 n == 1 이미 포함한거 아닌가? 계산식을 밖에서 계산할 경우
            if n % 2 == 1:
                return loop(m+m, n//2, k+m)
                # loop 함수 안에서 계산해줘야 하는거 아닌가? 계산식을 밖에서 계산할 경우
            else:
                return loop(m+m, n//2, k)
        else:
            return k
    # 질문: 여기 if 문을 꼭 넣어야 하는 건가??
    # if n > 0:
    #     return loop(m,n,0)
    # else:
    #     return 0
    return loop(m, n, 0)


print(R(57,86))



#while 루프
def R(m,n):
    k = 0
    while n > 0:
        if n % 2 == 1:
            m, n, k = 2*m, n//2, k+m
        else:
            m, n= 2 * m, n // 2
    return k
print(R(57,86))

# while 루프 수정
def R(m,n):
    k = 0
    while n > 0:
        if n % 2 == 1:
            k = k+m
        m, n = 2 * m, n // 2
    return k


print(R(57,86))
print(R(57,0))


