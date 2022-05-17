def run_comb_pascal(n, r):
    from time import perf_counter
    start = perf_counter()
    answer = comb_pascal(n, r)
    finish = perf_counter()
    print('comb(',n,',', r,') => ', answer, sep='')
    print(round(finish-start, 4), 'seconds')
