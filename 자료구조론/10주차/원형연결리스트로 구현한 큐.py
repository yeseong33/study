class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link


class CircularLinkedQueue:

    def __init__(self):
        self.tail = None

    def isEmpty(self): return self.tail == None
    def clear(self): self.tail = None

    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
                return data

    def size(self):
        if self.isEmpty(): return 0
        else:
            count = 1
            node = self.tail.link
            while node != self.tail:
                node = node.link
                count += 1
            return count

    def display(self):
        if self.isEmpty(): print('비어있습니다.')
        else:
            node = self.tail.link
            print('CircularLinkedQueue: ', end='')
            while node != self.tail:
                print(node.data, end=' ')
                node = node.link
            print(node.data)


q = CircularLinkedQueue()
for i in range(8): q.enqueue(i)
q.display()
for i in range(5): q.dequeue()
q.display()
for i in range(8, 14): q.enqueue(i)
q.display()

