class DList:
    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def insert(self, item):
        f = self.head
        n = self.Node(item, f, f.next)
        f.next.prev = n
        f.next = n
        self.size += 1

    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)
        t.next = n
        p.prev = n
        self.size += 1

    def insert_after(self, p, item):
        t = p.next
        n = self.Node(item, p, t)
        t.prev = n
        p.next = n
        self.size += 1

    def delete_h(self, x):
        p = x.prev
        t = x.next
        p.next = t
        t.prev = p
        self.size -= 1
        return x.item

    def search(self, target):
        p = self.head.next
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next
        return None

    def add(self, r, e):
        if self.is_empty():
            self.insert(e)
        elif self.size < r:
            self.insert_after(self.tail.prev, e)
        else:
            p = self.head.next
            while self.search(p.item)+1 != r:
                p = p.next
            self.insert_before(p, e)

    def delete(self, r):
        p = self.head.next
        while self.search(p.item) + 1 != r:
            p = p.next
        self.delete_h(p)

    def get(self, r):
        if self.size < r:
            return print('invalid position')
        p = self.head.next
        while self.search(p.item)+1 != r:
            p = p.next
        return print(p.item)

    def print(self):
        if self.is_empty():
            return print('리스트 비어있음')
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.item, end='')
            else:
                print(p.item)
            p = p.next
        return None


class EmptyError(Exception):
    pass


num = int(input('연산의 개수 : '))
s = DList()
for i in range(num):
    inputs = input('Input : ')
    operation = inputs[0]
    if operation == 'A':
        pos = int(inputs[2:-1])
        alphabet = inputs[-1]
        s.add(pos, alphabet)
    elif operation == 'D':
        pos = int(inputs[2:])
        s.delete(pos)
    elif operation == 'G':
        pos = int(inputs[2:])
        s.get(pos)
    elif operation == 'P':
        s.print()



