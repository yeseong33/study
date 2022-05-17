def selection_sort(xs):
    if xs != []:
        m = min(xs)
        xs.remove(m)
        return [m]+selection_sort(xs)
    else:
        return []


l = [4, 1, 2, 5, 3]
print(selection_sort(l))


def selection_sort(xs):
    def loop(xs, ss):
        if xs != []:
            m = min(xs)
            xs.remove(m)
            ss.append(m)
            return loop(xs, ss)
        else:
            return ss
    return loop(xs, [])


l = [4, 1, 2, 5, 3]
print(selection_sort(l))


def selection_sort(xs):
    ss = []
    while xs != []:
        m = min(xs)
        xs.remove(m)
        ss.append(m)
    return ss

l = [4,1,2,5,3]
print(selection_sort(l))