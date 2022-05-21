# # 봉지 2, 3, 5
# # 주문 2키로 이상만
# # 봉지의 수가 최소가 되도록 포장
# # 18 = 5 5 5 3
#
#
# def minbegs(kg):
#     kg_5 = kg // 5
#     kg_3 = kg % 5 // 3
#     kg_2 = kg % 5 % 3
#     b = kg_2 + kg_3 + kg_5
#     return b
#
#
def minbegs(kg):
    if kg > 1:
        if kg == 2 or kg == 3 or kg == 5:
            return 1
        else:
            smallest = minbegs(kg-2)
            if kg > 4:
                smallest = min(smallest, minbegs(kg-3))
            if kg > 6:
                smallest = min(smallest, minbegs(kg-5))
        return 1 + smallest
    else:
        return 0
#
#
# def minbeg(n):
#     begs = [0, 0, 1, 1, 2, 1, 2]
#     if n > 6:
#         for i in range(7, n+1):
#             smallest = min(begs[i-2], begs[i-3], begs[i-5])
#             begs.append(smallest+1)
#     return begs[n]
#
#
# def run_minbegs(n):
#     from time import perf_counter
#     start = perf_counter()
#     answer = minbegs(n)
#     finish = perf_counter()
#     print('minbegs(',n,') =>', answer, sep='')
#     print(round(finish-start, 1), 'seconds')
#
# run_minbegs(123)
#
#
# def moon(m):
#     if m > 0:
#         if m == 1 or m == 2 or m == 5 or m == 7:
#             return 1
#         elif m in [3,4,6]:
#             return 2
#         else:
#             smallset = min(moon(m-1), moon(m-2), moon(m-5), moon(m-7))
#             return smallset + 1
#     else:
#         return 0

#
# print(moon(12))


def moon(m):
    a = [0, 1, 1, 2, 2, 1, 2, 1]
    if m > 7:
        for i in range(8, m+1):
            smallest = min(a[i-1], a[i-2], a[i-5], a[i-7])
            a.append(1+smallest)
    return a[m]


def run_minbegs(n):
    from time import perf_counter
    start = perf_counter()
    answer = moon(n)
    finish = perf_counter()
    print('moon(',n,') =>', answer, sep='')
    print(round(finish-start, 1), 'seconds')


for i in range(1, 12):
    run_minbegs(i)


