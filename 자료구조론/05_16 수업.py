class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

f4 = TNode(70, None, None)
f5 = TNode(90, None, None)
f2 = TNode(30, f4, f5)
f7 = TNode(130, None, None)
f8 = TNode(80, None, None)
f6 = TNode(120, f7, f8)
f3 = TNode(50, None, f6)
f1 = TNode(20, f2, f3)

l = [f1, f2, f3, f4, f5, f6, f7, f8]

i = int(input()) - 1

if i > 7:
    print(-1)
elif l[i].left == None and l[i].right == None:
    print(l[i].data)
elif l[i].left != None and l[i].right != None:
    print(l[i].data, l[i].left.data, l[i].right.data)
elif l[i].left == None:
    print(l[i].data,l[i].right.data)
elif l[i].right == None:
    print(l[i].data, l[i].left.data)






