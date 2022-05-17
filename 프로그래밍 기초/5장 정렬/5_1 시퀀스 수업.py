#
# 1248
# 139
#
# 1 2 4 8
# 1 2 4 8 16
#  1 2 3 4 6 12
# 1 3 5 15
x = 0

for n in range(1,1001):
    sum = 0
    for i in range(n):
        if n % (i + 1) == 0:
            x = n // (i + 1)
            if x > i + 1:
                sum += x + (i + 1)
            elif x == i + 1:
                sum += x
            else:
                sum_f = sum - n
                if sum_f == n:
                    print(sum_f,'는 완전수')
                break
