# (1) str-int 사용(처음 생각한 거)
N = '{:02}'.format(int(input()))
N_b = int(N)
i = 0
while True:
    k = '{:02}'.format(int(N[0]) + int(N[1]))
    N = N[1]+k[1]
    i += 1
    if int(N) == N_b:
        print(i)
        break


# (2) 수식 사용
N = int(input())
key = N
i = 0
while True:
    k = (N // 10) + (N % 10)
    N = (N % 10) * 10 +(k % 10)
    i += 1
    if N == key:
        print(i)
        break