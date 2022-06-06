# 중첩루프
# couples = []
# for c in ['a', 'b']:
#     for n in range(3):
#         couple = (c, n)
#         couples.append(couple)
# print(couples)


# 아스키 아트

# def digital_art_horizontal(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             print(j, end=' ')
#         print('')
#
#
# digital_art_horizontal(7)
#
#
# def digital_art_horizontal_left_down(n):
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print(j, end=' ')
#         print('')
#
#
# digital_art_horizontal_left_down(7)


# def digital_art_horizontal_left_up(n):
#     for i in range(1, n+1):
#         for j in range(1, n-i+2):
#             print(j, end=' ')
#         print('')
#
#
# digital_art_horizontal_left_up(7)


# def digital_art_vertical(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             print(i, end=' ')
#         print('')
#
#
# digital_art_vertical(7)
#
#
# def digital_art_vertical_right_down(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if j <= n-i:
#                 print(' ', end=' ')
#             else:
#                 print(i, end=' ')
#         print('')
#
#
# digital_art_vertical_right_down(7)
#
#
# def digital_art_horizontal_alternate(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i % 2 == 0:
#                 print(n-j+1, end=' ')
#             else:
#                 print(j, end=' ')
#         print('')
#
#
# digital_art_horizontal_alternate(7)
#
#
# def digital_art_vertical_alternate(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if j % 2 == 0:
#                 print(n-i+1, end=' ')
#             else:
#                 print(i, end=' ')
#         print('')
#
#
# digital_art_vertical_alternate(7)


# 버블정렬
# s = [32,23,18,7,11,99,55]
#
#
# def bubble_sort(s):
#     for i in range(len(s)):
#         for j in range(len(s)-1):
#             if s[j] > s[j+1]:
#                 s[j], s[j+1] = s[j+1], s[j]
#     return s
#
#
# print(bubble_sort(s))

s = ["0508", "0515", "1225", "0915", "1111", "0101", "0318", "0301", "0815"]


def radix_sort(s):
    for i in range(len(s[0])):
        k = [[] for _ in range(10)]
        for j in range(len(s)):
            k[int(s[j][3-i])].append(s[j])
        s = sum(k, [])

    return s


print(radix_sort(s))


def radix_sort(ds):
    if ds != []:
        length = len(ds[0])
        for i in range(length-1, -1, -1):
            distributed = [[] for _ in range(10)]
            for d in ds:
                distributed[int(d[i])].append(d)
            ds = []
            for d in distributed:
                ds += d
        return ds
    else:
        return []


print(radix_sort(s))

