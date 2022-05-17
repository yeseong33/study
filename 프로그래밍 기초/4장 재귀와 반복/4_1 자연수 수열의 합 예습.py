# 일반 재귀
def sumrange(m,n):
    if m <= n:
        return m + sumrange(m+1,n)
    else:
        return 0

# Test code
print(sumrange(3,2))   # 0
print(sumrange(3,3))   # 3
print(sumrange(3,4))   # 7
print(sumrange(3,6))   # 18
print(sumrange(1,10))  # 55
print(sumrange(-5,10)) # 40
print(sumrange(-5,-2)) # -14


# 꼬리 재귀
def sumrange(m,n):
    def loop(m,total):
        if m <= n:
            return loop(m+1,m+total)
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



# while 루프
def sumrange(m,n):
    total = 0
    while m <= n:
        total = total + m
        m = m+1
    return total

print(sumrange(3,2))   # 0
print(sumrange(3,3))   # 3
print(sumrange(3,4))   # 7
print(sumrange(3,6))   # 18
print(sumrange(1,10))  # 55
print(sumrange(-5,10)) # 40
print(sumrange(-5,-2)) # -14
