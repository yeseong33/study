# 지난시간 보충
# def isleapyear(y):
#     if y >= 0:
#         return y % 4 == 0 and y % 100 != 0 or \
#                y % 400 == 0
#     else:
#         return None
#
# print(isleapyear(2008))
# print(isleapyear(2008))
# print(isleapyear(2008))
#
# print(isleapyear(1999))
# print(isleapyear(1998))
# print(isleapyear(1997))
#
# print(isleapyear(2800))
# print(isleapyear(2400))
# print(isleapyear(2000))
#
# print(isleapyear(2100))
# print(isleapyear(2200))
# print(isleapyear(2300))

# 가능한 논리를 직관적으로 쓰고나서 정리한다.


# def sigma(n):
#     if n > 0:
#         return sigma(n-1) + n
#     else:
#         return 0
# print(sigma(14))
# sigma() 함수를 위에서 아래쪽으로 계속해서 부르면서 계산한다.



def sigma(n):
    return loop(n,0)

def loop(n,total):
    if n > 0:
        return loop(n-1,total+n)
    else:
        return total

# 위 두함수를 지역화를 통해 다음과 같이 나타낼 수 있다.

def sigma(n):

# 지역화
    def loop(n,total):
        if n > 0:
            return loop(n-1,total+n)
        else:
            return total

    return loop(n,0)

print(sigma(99))


def sigma(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

print(sigma(44400))

def sigma(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total

print(sigma(44400))



# def subrange(m,n):
#     if m <= n:
#         return m + subrange(m+1,n)
#     else:
#         return 0

def sumrange(m,n):
    def loop(m,total):
        if m <=n:
            return loop(m+1,total+m)
        else:
            return total
    return loop(m,0)

print(sumrange(3,2))   # 0
print(sumrange(3,3))   # 3
print(sumrange(3,4))   # 7
print(sumrange(3,6))   # 18
print(sumrange(1,10))  # 55
print(sumrange(-5,10)) # 40
print(sumrange(-5,-2)) # -14

def subrange1(m,n):
    total = 0
    while m <= n:
        # 순서 중요 ** -> total 값에 영향을 주기 때문
        total += m
        m += 1
    return total

print(subrange1(3,2))   # 0
print(subrange1(3,3))   # 3
print(subrange1(3,4))   # 7
print(subrange1(3,6))   # 18
print(subrange1(1,10))  # 55
print(subrange1(-5,10)) # 40
print(subrange1(-5,-2)) # -14
## 재귀, 꼬리, while 반복문 순서대로의 과정 이해하는 것 중요
