# 재귀함수
def s_search(s, x):
    mid = len(s)//2
    if s != []:
        if s[mid] == x:
            return True
        elif s[mid] > x:
            return s_search(s[:mid], x)
        else:
            return s_search(s[mid+1:], x)
    else:
        return False


s = [1,2,3,4,5,6,7,8,9]
print(s_search(s, 5))
print(s_search(s, 1))
print(s_search(s, 8))
print(s_search(s, 11))


# while 루프
def s_search(s, x):
    while s != []:
        mid = len(s) // 2
        if s[mid] < x:
            s = s[mid+1:]
        elif s[mid] > x:
            s = s[:mid]
        else:
            return True
    return False


s = [1,2,3,4,5,6,7,8,9]
print(s_search(s, 5))
print(s_search(s, 1))
print(s_search(s, 8))
print(s_search(s, 11))


# 논리식
def s_search(s, x):
    mid = len(s) // 2
    return s != [] and \
           (s[mid] == x or
            s[mid] > x and s_search(s[:mid], x) or
            s[mid] < x and s_search(s[mid+1:], x))


s = [1,2,3,4,5,6,7,8,9]
print(s_search(s, 5))
print(s_search(s, 1))
print(s_search(s, 8))
print(s_search(s, 11))


# 이분 검색 알고리즘
def s_search_index(s, x):
    low = 0
    high = len(s)-1
    while low <= high:
        mid = (low + high) // 2
        if x == s[mid]:
            return mid
        elif x < s[mid]:
            high = mid -1
        else:
            low = mid + 1
    return None


s = [1,2,3,4,5,6,7,8,9]
print(s_search_index(s, 5))
print(s_search_index(s, 1))
print(s_search_index(s, 8))
print(s_search_index(s, 11))


