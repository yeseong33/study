# 재귀함수를 사용
# def power(b, n):
#     if n > 0:
#         return b * power(b, n-1)
#     else:
#         return 1
#
# print(power(2,5))

# 계산비용 분석 시간, 공간
# 시간: 곱셈의 횟수(= 재귀합수를 호출하는 횟수)에 비례
# 인수가 n 일 때 곱셈을 총 n번 하므로 계산시간은 n에 비례
# 공간: 재귀함수를 호출하는 횟수에 비례(답을 구해온 뒤에 곱해야 할 수를 기억해둘 공간 필요)
# 인수가 n일 때 재귀호출을 총 n번 하므로 필요공간은 n에 비례

# 꼬리재귀
# def power(b, n):
#     def loop(n, prod):
#         if n > 0:
#             return loop(n-1, b*prod)
#         else:
#             return prod
#     return loop(n, 1)
#
# print(power(2,5))

# 계산비용 분석
# 시간: 곱셈의 횟수(= 재귀 함수를 호출하는 횟수)에 비례
# 인수가 n일 때 곱셈을 총 n번(=제귀 호출을 총 n번) 하므로 계산시간은 n에 비례
# 공간: 인수의 크기와 상관없이 일정

# while 루프
# def poewr(b, n):
#     prod = 1
#     while n > 0:
#         prod = b * prod
#         n = n - 1
#     return prod
# 계산 비용 꼬리 재귀와 같다.


def power(b, n):
    if n > 0:
        if n % 2 == 0:
            return power(b * b, n//2)
        else:
            return b * power(b, n-1)
    else:
        return 1

print(power(2,13))

# 꼬리재귀
def power(b, n):
    def loop(b, n, prod)
        if n > 0:
            if n % 2 == 0:
                return loop(b * b, n//2, prod)
            else:
                return loop(b, n-1, b * prod)
        else:
            return prod
    return loop(b, n, 1)

def power(b, n):
    prod = 1
    while n >0:
        if n % 2 == 0:
            b = b * b
            n = n // 2
        else:
            n = n - 1
            prod = b * prod
    return prod
