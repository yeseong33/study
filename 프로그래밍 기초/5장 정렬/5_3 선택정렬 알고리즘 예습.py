def selection_sort(s):
    if s != []:
        m = min(s)
        s.remove(m)
        return [m] + selection_sort(s)
    else:
        return []


l = [4,1,2,5,3]
print(selection_sort(l))


def selection_sort(s):
    def loop(s, k):
        if s != []:
            m = min(s)
            s.remove(m)
            k.append(m)
            return loop(s, k)
        else:
            return k
    return loop(s, [])


l = [4,1,2,5,3]
print(selection_sort(l))


def selection_sort(s):
    k = []
    while s != []:
        m = min(s)
        s.remove(m)
        k.append(m)
    return k


l = [4,1,2,5,3]
print(selection_sort(l))

