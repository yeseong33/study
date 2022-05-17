# 원형 연결리스트의 응용: 연결된 큐
# tail을 사용하는 것이 rear와 front에 바로 접근할 수 있다는 점에서 훨씬 효율적이다.
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
            while not node == self.tail:
                node = node.link
                count += 1
            return count
#
# q = CircularLinkedQueue()
# q.enqueue(1)
# print(q.size())

# 덱
# 스택이나 큐보다 입출력이 자유로운 구조
# 전단과 후단에서 모두 삽입, 삭제가 가능하다.
MAX_QSIZE =10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None]*MAX_QSIZE

    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1)%MAX_QSIZE

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print('[f=%d,r=%d]'%(self.front, self.rear), out)


class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front-1
            if self.front < 0: self.front = MAX_QSIZE-1

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1
            if self.rear <0 : self.rear = MAX_QSIZE -1
            return item
    def getRear(self):
        return self.items[self.rear]









