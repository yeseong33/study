# def merge(left, right):
#     if left != [] and right != []:
#         if left[0] < right[0]:
#             return [left[0]] + merge(left[1:], right)
#         else:
#             return [right[0]] + merge(left, right[1:])
#     else:
#         return left + right


# def merge(left, right):
#     def loop(left, right, k):
#         if left != [] and right != []:
#             if left[0] <= right[0]:
#                 return loop(left[1:], right,k + [left[0]])
#             else:
#                 return loop(left, right[1:],k + [right[0]])
#         else:
#             return k + left + right
#     return loop(left, right, [])


# def merge(left, right):
#     k = []
#     while left != [] and right != []:
#         if left[0] <= right[0]:
#             k.append(left[0])
#             left = left[1:]
#             print(left,'left')
#         else:
#             k.append(right[0])
#             right = right[1:]
#             print(right,'right')
#     return k + left + right
#
# # for 루프로 불가능 하다.
#
#
# def merge_sort(xs):
#     if len(xs) > 1:
#         mid = len(xs) // 2
#         return merge(merge_sort(xs[:mid]), merge_sort(xs[mid:]))
#     else:
#         return xs
#
#
# print(merge_sort([9,5,8,7,6,4,3,1,2]))
#
# def quicksort(xs):
#     if len(xs) > 1:
#         pivot = xs[0]
#         (left, right) = partition(pivot, xs[1:])
#         return quicksort(left) + [pivot] + quicksort(right)
#     else:
#         return xs
#
# def partition(p, s):
#     if s != []:
#         left, right = partition(p, s[1:])
#         if s[0] <= p:
#             left.append(s[0])
#         else:
#             right.append(s[0])
#         return left,right
#     else:
#         return [], []
#
#
# def partition(p, s):
#     def loop(s,left,right):
#         if s != []:
#             if s[0] < p:
#                 left.append(s[0])
#             else:
#                 right.append(s[0])
#             return loop(s[1:], left, right)
#         else:
#             return left, right
#     return loop(s, [], [])


# def patition(p, s):
#     left, right = [],[]
#     for x in s:
#         if x <= p:
#             left.append(x)
#         else:
#             right.append(x)
#     return left, right

# 다시 혼자 해보기!





# 팰린드롬 검사 함수 시험 ##

# def ispalindrome(s):
#     if len(s) <= 1:
#         return True
#     elif s[0] != s[-1]:
#         return False
#     else:
#         return ispalindrome(s[1:-1])


def ispalindrome(s):
    return len(s) <= 1 or s[0] == s[-1] and ispalindrome(s[1:-1])



print(ispalindrome(''))
print(ispalindrome('a'))
print(ispalindrome('aa'))
