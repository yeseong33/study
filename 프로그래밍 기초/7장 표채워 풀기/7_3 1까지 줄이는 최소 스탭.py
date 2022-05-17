def minsteps(n):
    if n > 1:
        steps = minsteps(n-1)
        if n % 2 == 0:
            steps = min(steps, minsteps(n//2))
        if n % 3 == 0:
            steps = min(steps, minsteps(n//3))
        return 1 + steps
    else:
        return 0


print(minsteps(10))

def run_minsteps(n):
    from time import perf_counter
    start = perf_counter()
    answer = minsteps(n)
    finish = perf_counter()
    print('comb(',n,') => ', answer, sep='')
    print(round(finish-start, 4), 'seconds')


# run_minsteps(514)


def minsteps(n):
    memo = [0 for _ in range(n+1)]
    def loop(n):
        if n > 1:
            if memo[n] == 0:
                steps = loop(n-1)
                if n % 2 == 0:
                    steps = min(steps, loop(n//2))
                if n % 3 == 0:
                    steps = min(steps, loop(n//3))
                memo[n] = steps + 1
            return memo[n]
        else:
            return 0
    return loop(n)


print(minsteps(10))

def run_minsteps(n):
    from time import perf_counter
    start = perf_counter()
    answer = minsteps(n)
    finish = perf_counter()
    print('comb(',n,') => ', answer, sep='')
    print(round(finish-start, 4), 'seconds')

run_minsteps(900)


def minsteps(n):
    memo = [0 for _ in range(n+1)]
    def loop(n):
        if n > 1:
            if memo[n] == 0:
                steps = loop(n-1)
                if n % 2 == 0:
                    steps = min(steps, loop(n//2))
                if n % 3 == 0:
                    steps = min(steps, loop(n//3))
                memo[n] = steps + 1
            return memo[n]
        else:
            return 0
    return loop(n)
# print(minsteps(10))



def minsteps(n):
    memo = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if n > 1:
            if memo[n] == 0:
                steps = n-1
                if n % 2 == 0:
                    steps = min(steps, n//2)
                if n % 3 == 0:
                    steps = min(steps, n//3)
                memo[n] = steps + 1
            else:
                memo[n] = 0
        else:
            return 0
    return memo[n]

# print(minsteps(10))
#







