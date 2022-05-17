def bin_search_OX(ss, x):
    if ss != []:
        mid = len(ss) // 2
        if x == ss[mid]:
            return True
        elif x < ss[mid]:
            return bin_search_OX(ss[:mid], x)
        else:
            return bin_search_OX(ss[mid:], x)
    else:
        return False


def bin_search_OX(ss, x):
    while ss != []:
        mid = len(ss) // 2
        if x == ss[mid]:
            return True
        elif x < ss[min]:
            ss = ss[:mid]
        else:
            ss = ss[mid:]
    return False


# def bin_search_OX(ss, x):
#     mid = len(ss) // ss
#     return ss != [] and x == ss[mid] or


def bin_search_OX(ss, x):
    if ss != []:
        mid = len(ss) // 2
        if x == ss[mid]:
            return True
        elif x < ss[mid]:
            return bin_search_OX(ss[:mid], x)
        else:
            return bin_search_OX(ss[mid+1:], x) # mid는 이미 검사했기 때문에
    else:
        return False

def bin_search_OX(ss, x):
    while ss != []:
        mid = len(ss) // 2
        if x == ss[mid]:
            return True
        elif x < ss[mid]:
            ss = ss[:mid]
        else:
            ss = ss[mid+1:]
    return False

def bid_search_OX(ss, x):
    mid = len(ss)//2
    return ss != [] and \
           (x == ss[mid] or
            x < ss[mid] and bid_search_OX(ss[:mid],x) or
            x > ss[mid] and bid_search_OX(ss[mid+1:],x))

print(bid_search_OX([1,2,3,4,5,6,7,8,9],11))