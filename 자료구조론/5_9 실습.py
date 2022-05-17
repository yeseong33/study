class DNode:
    def __init__ (self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__( self ):
        self.front = None
        self.rear = None

    def isEmpty( self ): return self.front == None

    def addFront( self, item ):
        node = DNode(item, None, self.front)
        if( self.isEmpty()):
            self.front = self.rear = node
        else :
            self.front.prev = node
            self.front = node

    def addRear( self, item ):
        node = DNode(item, self.rear, None)
        if( self.isEmpty()):
            self.front = self.rear = node
        else :
            self.rear.next = node
            self.rear = node

    def deleteFront( self ):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front==None :
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear( self ):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear==None :
                self.front = None
            else:
                self.rear.next = None
            return data

    def display( self, msg='□'):
        print(msg, end='')
        node = self.front
        while not node == None :
            print(node.data, end=' ')
            node = node.next
        print()


num = int(input(''))
dq = DoublyLinkedDeque()
for i in range(num):
    inputs = input('')
    o = inputs.split()
    operation = o[0]
    if operation == 'AF':
        k = int(o[1])
        dq.addFront(k)

    elif operation == 'AR':
        k = int(o[1])
        dq.addRear(k)

    elif operation == 'DF':
        if dq.isEmpty():
            print('underflow')
            break
        else:
            dq.deleteFront()

    elif operation == 'DR':
        if dq.isEmpty():
            print('underflow')
            break
        else:
            dq.deleteRear()
    elif operation == 'P':
        dq.display()

