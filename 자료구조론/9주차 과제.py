class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [0]*MAX_QSIZE

    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1)%MAX_QSIZE

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            self.items[self.front] = 0

    def display(self):
        return self.items


MAX_QSIZE = int(input(''))
q = CircularQueue()
num = int(input(''))
for i in range(num):
    inputs = input('')
    operation = inputs[0]
    if operation == 'I':
        k = int(inputs[2:])
        if q.isFull():
            print('overflow□', end='')
            for i in range(MAX_QSIZE):
                if i != MAX_QSIZE-1:
                    print(q.display()[i], end=' ')
                else:
                    print(q.display()[i])
            break
        else:
            q.enqueue(k)
    elif operation == 'D':
        if q.isEmpty():
            print('underflow')
            break
        else:
            q.dequeue()
    elif operation == 'P':
        print('□', end='')
        for i in range(MAX_QSIZE):
            if i != MAX_QSIZE-1:
                print(q.display()[i], end=' ')
            else:
                print(q.display()[i])
