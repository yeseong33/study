def push(item):
    steak.append(item)


def peek():
    if len(steak) != 0:
        return steak[-1]


def pop():
    if len(steak) != 0:
        item = steak.pop(-1)
        return item

steak = []

push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후:\t', end='')
print(steak, '\t<- top')
print('top 항목: ',end='')
print(peek())
push('pear')
print('배 push 후:\t\t', end='')
print(steak, '\t<- top')
pop()
push('grape')
print('pop(), 포도 push 후:\t', end='')
print(steak, '\t<- top')