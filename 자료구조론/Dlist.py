# class Dlist:
#     class Node:
#         def __init__(self, item, prev, link):
#             self.item = item
#             self.prev = prev
#             self.next = link
#
#     def __init__(self):
#         self.head = self.Node(None, None, None)
#         self.tail = self.Node(None, self.head, None)
#         self.head.next = self.tail
#         self.size = 0
#
#     def size(self): return self.size
#     def is_empty(self): return self.size == 0
#
#
#     def insert(self, item):
#         f = self.head
#         n = self.Node(item, f, f.next)
#         f.next.prev = n
#         f.next = n
#         self.size += 1
#
#     def insert_before(self, p, item):
#         t = p.prev
#         n = self.Node(item, t, p)
#         t.next = n
#         p.prev = n
#         self.size += 1
#
#     def insert_after(self, p, item):
#         t = p.next
#         n = self.Node(item, p, t)
#         t.prev = n
#         p.next = n
#         self.size += 1
#
#     def delete(self, x):
#         p = x.prev
#         t = x.next
#         p.next = t
#         t.prev = p
#         self.size -= 1
#         return x.item
#
#     def search(self, target):
#         p = self.head.next
#         for k in range(self.size):
#             if target == p.item: return k
#             p = p.next
#         return None
#
#
#     def add(self, r, e):
#         if self.is_empty():
#             self.insert(e)
#         elif  self.size < r:
#             self.insert_after(self.tail.prev ,e)
#         else:
#             p = self.head.next
#             while s.search(p.item) + 1 != r:
#                 p = p.next
#             self.insert_before(p,e)
#
#
#
#
#
#
#
#
#
#     def l_delete(self, r):
#         p = self.head.next
#         while s.search(p.item) + 1 != r:
#             p = p.next
#         self.delete(p)
#
#     def get(self, r):
#         p = self.head.next
#         while s.search(p.item) + 1 != r:
#             p = p.next
#         return p
#
#
#
#     def print_list(self):
#         if self.is_empty():
#             print('리스트 비어있음')
#         else:
#             p = self.head.next
#             while p != self.tail:
#                 if p.next != self.tail:
#                     print(p.item,' <-> ',end = '')
#                 else:
#                     print(p.item)
#                 p = p.next
#
# class EmptyError(Exception):
#     pass
#
#
#
#
# s = Dlist()
# # s.insert('S')
# # s.insert('1')
# # s.insert('2')
# # s.insert('3')
# s.add(1,'S')
# s.add(2,'t')
# s.add(3,'r')
# s.add(3,'a')
# s.print_list()
# s.insert_after(s.head,'apple')
# s.insert_before(s.tail, 'orange')
# s.insert_before(s.tail, 'cherry')
# s.insert_after(s.head.next,'peer')
# s.print_list()
# print('마지막 노드 삭제 후:\t', end='')
# s.delete(s.tail.prev)
# s.print_list()
# print('맨 끝에 포도 삽입 후:\t', end = '')
# s.insert_before(s.tail,'grape')
# s.print_list()
# print(s.search('peer'))
# s.add(3,'고록')
# s.print_list()
# s.l_delete(3)
# s.print_list()
# print('첫 노드 삭제 후:\t',end = '')
# s.delete(s.head.next)
# s.print_list()
# print('첫 노드 삭제 후:\t', end = '')
# s.delete(s.head.next)
# s.print_list()
# print('첫 노드 삭제 후:\t', end='')
# s.delete(s.head.next)
# s.print_list()
# print('첫 노드 삭제 후:\t', end='')
# s.delete(s.head.next)
# s.print_list()


class Dlist:
    class Node:
        def __init__(self, item, prev, link):
            self.item  = item
            self.prev = prev
            self.next = link

    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item,t,p)
        t.next = n
        p.prev = n
        self.size += 1

    def insert_after(self, p, item):
        t = p.next
        n = self.Node(item, p,t)
        p.next = n
        t.prev = n
        self.size += 1

    def delete(self,x):
        r = x.next
        f = x.prev
        f.next = r
        r.prev = f
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print('리스트 비어있음')
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                p = p.next

class EmptyError(Exception):
    pass



s = Dlist()
s.insert_after(s.head, 'apple')
s.insert_before(s.tail, 'orange')
s.insert_before(s.tail, 'cherry')
s.insert_after(s.head.next, 'pear')
s.print_list()
print('마지막 노드 삭제 후:\t', end='')
s.delete(s.tail.prev)
s.print_list()
print('맨 끝에 포도 삽입 후:\t', end='')
s.insert_before(s.tail, 'grape')
s.print_list()
print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()
print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()
print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()
print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()





