# def tower_of_hanoi(n, start, to, via):
#     if n > 1:
#         tower_of_hanoi(n-1, start, via, to)
#         print('Move a disk from', start, 'to', to)
#         tower_of_hanoi(n-1, via, to, start)
#     else:
#         print('Move a disk from', start, 'to', to)
#
# tower_of_hanoi(4, 'A','C','B')


def tower(n, start, via, to):
    if n > 1:
        tower(n-1, start, to, via)
        print('Move a disk from', start, 'to', to)
        tower(n-1, via, start, to)
    else:
        print('Move a disk from', start, 'to', to)

tower(3, 'a','b','c')



#
# def tower_of_hanoi(n, start, to, via):
#     global count
#     if n > 1:
#         tower_of_hanoi(n-1, start, via, to)
#         count += 1
#         tower_of_hanoi(n-1, via, to, start)
#     else:
#         count += 1
#
# for n in [4,6,8,16,24,25,26,27,28]:
#     count = 0
#     from time import perf_counter
#     start = perf_counter()
#     tower_of_hanoi(n, 'a', 'c', 'b')
#     finish = perf_counter()
#     cpu_time = round(finish-start, 1)
#     print(n, 'disk:', count, 'moves in', cpu_time,'seconds')
#
#
# 386547055200번 이동하면 하루가 지난다.
