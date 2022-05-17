def insert(x, k):
    if k != []:
        if x <= k[0]:
            return [x]+k
        else:
            return [k[0]] + insert(x, k[1:])
    else:
        return [x]


def insert(x, k):
    def loop(k, l):
        if k != []:
            if x <= k[0]:
                l.append(x)
                return l + k
            else:
                l.append(k[0])
                return loop(k[1:], l)
        else:
            l.append(x)
            return l
    return loop(k, [])


# 풀이
def insert(x,ss):
    def loop(ss, left):
        if ss !=[]:
            if x <= ss[0]:
                return left + [x] + ss
            else:
                return loop(ss[1:], left + [ss[0]])
        else:
            return left + [x]
    return loop(ss, [])



def insert(x, k):
    l = []
    while k != []:
        if x <= k[0]:
            l.append(x)
            return l + k
        else:
            l.append(k[0])
            k = k[1:]
    l.append(x)
    return l


def insertion_sort(s):
    if s != []:
        return insert(s[0], insertion_sort(s[1:]))
    else:
        return []


l = [4, 1, 2, 5, 3]
print(insertion_sort(l))


def insertion_sort(s):
    def loop(s, k):
        if s != []:
            return loop(s[1:], insert(s[0], k))
        else:
            return k
    return loop(s, [])


l = [4, 1, 2, 5, 3]
print(insertion_sort(l))


def insertion_sort(s):
    k = []
    while s != []:
        k = insert(s[0], k)
        s = s[1:]
    return k


l = [4, 1, 2, 5, 3]
print(insertion_sort(l))

# for 루프가 나은가 아니면 while이 나은가


