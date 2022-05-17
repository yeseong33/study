class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]


def checkBrackets(statement):
    stack = Stack()
    n = 0
    w = 0
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
            n += 1
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                n += 1
                w += 1
            else:
                left = stack.pop()
                n += 1
                if (ch == '}' and left != '{') or \
                    (ch == ']' and left != '[') or \
                    (ch == ')' and left != '('):
                    w += 1
    if stack.isEmpty() == False:
        w += 1
    return n, w


# 괄호 짝 유효성 검사 프로그램
statement = input('')
n = checkBrackets(statement)[0]
w = checkBrackets(statement)[1]
if w > 0:
    print('Wrong_'+str(n))
else:
    print('OK_'+str(n))


