def seq_search_OX(s, x):
    if s != []:
        if s[0] == x:
            return True
        else:
            return seq_search_OX(s[1:], x)
    else:
        return False


def seq_search_OX(s, x):
    def loop(s):
        if s != []:
            if s[0] == x:
                return True
            else:
                return loop(s[1:])
        else:
            return False
    return loop(s)


def seq_search_OX(s, x):
    while s != []:
        if s[0] == x:
            return True
        else:
            s = s[1:]
    return False


def seq_search_OX(s, x):
    for key in s:
        if key  == x:
            return True
    return False


def seq_search_OX(s, x):
    return s != [] and (s[0] == x or (s[0] != 0 and seq_search_OX(s[1:], x)))



def seq_search_OX(s, x):
    if s != []:
        if s[0] == x:
            return True
        else:
            return seq_search_OX(s[1:],x)
    else:
        return False

def seq_search(s, x):
    def loop(i):
        if s != []:
            if s[i] == x:
                return i
            else:
                return loop(i+1)
        else:
            return None
    return loop(0)

def seq_search(s, x):
    i = 0
    while i < len(s):
        if s[i] == x:
            return i
        else:
            i += 1
    return None

def seq_search(s, x):
    for i in range(len(s)):
        if s[i] == x:
            return i
    return None





