# 사전 지식
# ds = "2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376"
# def digit_frequencies(ds):
#     digit_count = [0 for _ in range(10)]
#     for d in ds:
#         digit_count[int(d)] += 1
#     paired = []
#     i = 0
#
#     for dc in digit_count:
#         paired.append((str(i), dc))
#         i += 1
#     return paired
#
# print(digit_frequencies(ds))
#
#
# def digit_frequencies_sort(ds):
#     paired = digit_frequencies(ds)
#     paired.sort(key = lambda x: x[1], reverse = True)
#     return paired
#
# print(digit_frequencies_sort(ds))


# 문제
def digit_ranking_board(txt):
    infile = open(txt, 'r')
    text = infile.read()
    infile.close()
    outfile = open('ranking.txt', 'w')
    digit_count = [0 for _ in range(10)]
    for d in text:
        digit_count[int(d)] += 1
    paired = []
    i = 0
    for dc in digit_count:
        paired.append((str(i), dc, str(round(dc / len(text) * 100, 1)) +'%'))
        i += 1
    paired.sort(key=lambda x:x[1], reverse=True)
    for k in range(10):
        outfile.write(paired[k][0] + ' ' + str(paired[k][1]) + ' ' + paired[k][2] + '\n')
    outfile.close()
    print('Done')

digit_ranking_board('digits.txt')