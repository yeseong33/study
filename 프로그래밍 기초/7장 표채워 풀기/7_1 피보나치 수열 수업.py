def fib(n):
    if n > 1:
        i = 2
        a, b = 0, 1
        while i <= n:
            a, b = b, a+b
            i += 1
        return b
    else:
        return n


# print(fib(0))


def fib(n):
    if n > 1:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
    else:
        return n


# print(fib(13))


# 알고리즘의 특징을 파악하는 것이 중요함


def fibseq(n):
    fibs = [0,1]
    for i in range(2, n+1):
        fibs.append(fibs[i-2] + fibs[i-1])
    return fibs


# print(fibseq(13))


def fib(n):
    return fibseq(n)[-1]


# print(fib(13))


def comb(n, r):
    if r != 0 and r != n:
        return comb(n-1, r-1) + comb(n-1, r)
    else:
        return 1


def run_comb(n, r):
    from time import perf_counter
    start = perf_counter()
    answer = comb(n, r)
    finish = perf_counter()
    print('comb(',n,',', r,') => ', answer, sep='')
    print(round(finish-start, 4), 'seconds')

# run_comb(30,19)


def comb_pascal(n, r):
    row0 = [1 for _ in range(r+1)]
    matrix = [row0] +[[1] for _ in range(n-r)]
    for i in range(1, n-r+1):
        for j in range(1, r+1):
            newvlaue = matrix[i][j-1] + matrix[i-1][j]
            matrix[i].append(newvlaue)
    return matrix[n-r][r]


# print(comb_pascal(30,19))

def run_comb_pascal(n, r):
    from time import perf_counter
    start = perf_counter()
    answer = comb_pascal(n, r)
    finish = perf_counter()
    print('comb(',n,',', r,') => ', answer, sep='')
    print(round(finish-start, 4), 'seconds')


run_comb_pascal(6,4)
