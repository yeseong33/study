# 재귀함수
def search(s, x):
    if s != []:
        if s[0] == x:
            return True
        else:
            return search(s[1:], x)
    else:
        return False


print(search([3,4,5,2],4))
print(search([3,4,5,2],6))


# while 함수
def search(s, x):
    while s !=[]:
        if s[0] == x:
            return True
        else:
            s = s[1:]
    return False


print(search([3,4,5,2],4))
print(search([3,4,5,2],6))


# for 루프
def search(s, x):
    for i in s:
        if i == x:
            return True
    return False


print(search([3,4,5,2],4))
print(search([3,4,5,2],6))


# 논리식
def search(s, x):
    return s != [] and \
           (s[0] == x or search(s[1:],x))


print(search([3,4,5,2],4))
print(search([3,4,5,2],6))


# index 찾는 검색
def search_index(s, x):
    def loop(i):
        if i != len(s):
            if s[i] == x:
                return i
            else:
                return loop(i+1)
        else:
            return None
    return loop(0)

print(search_index([3,4,5,2],4))
print(search_index([3,4,5,2],6))


# while 루프
def search_index(s, x):
    i = 0
    while i != len(s):
        if s[i] == x:
            return i
        i += 1
    return None


print(search_index([3,4,5,2],4))
print(search_index([3,4,5,2],6))


# for 루프
def search_index(s, x):
    for i in range(len(s)):
        if s[i] == x:
            return i
    return None


print(search_index([3,4,5,2],4))
print(search_index([3,4,5,2],6))
