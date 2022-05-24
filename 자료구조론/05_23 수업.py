# 힙 트리
# 더미와 모습이 비슷한 완전 이진트리 기반의 자료구조
# 가장 크거나 작은 값을 빠르게 찾아내도록 만들어진 자료 구조
# 최대 힙, 최소 힙

# 삽입식 힙트리
# 공백상태의 트리에 노드를 삽입

# 여러개의 키값을 받아들인 후
# 임의의 트리를 만든다.


# 힙: 삽입연산
# upheap
# 먼저 말단으로 들어간뒤 크기를 비교해 위치를 바꾼다.
# 시간 복잡도 O(log n)

# 힙: 삭제연산
# 최대힙에서
# 항상 루트가 삭제됨
# 가장 큰 키값을 가진 노드를 삭제
# 가장 낮은 노드를 루트로 올림
# 비교하며 내려옴
# 시간복잡도 O(logn)


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)
        # 인덱스 0은 사용하지 않기 때문에 0으로 채워 넣어준다.

    def size(self): return len(self.heap) - 1  # 0번 인덱스 사용 x
    def isEmpty(self): return self.size() == 0
    def Parent(self, i): return self.heap[i//2]
    def Left(self, i): return self.heap[i*2]
    def right(self, i): return self.heap[i*2+1]

    def display(self, msg = '힙트리: '):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while i != 1 and n > self.Parent(i):
            self.heap[i] = self.Parent(i)
            i = i // 2
        self.heap[i] = n

    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while child <= self.size():
                if child < self.size() and self.Left(parent) < self.right(parent):
                    child += 1
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot

heap = MaxHeap()
data = [2, 5, 4, 8, 9, 3, 7, 3]
print('[삽입연산] : '+ str(data))
for elem in data:
    heap.insert(elem)
heap.display()





class BHeap:
    def __init__(self, a):
        self.a = a
        self.N = len(a)-1

    def create_heap(self):
        for i in range(self.N//2, 0, -1):
            self.downheap(i)

    def insert(self, key_value):
        self.N += 1
        self.a.append(key_value)
        self.upheap(self.N)




# 탐색트리

# 이진탐색
# *정렬된* 데이터의 중간에 위치한 항목을 기준으로 데이터를 두 부분으로 나누어 가며
# 특정 항목을 찾는 탐색방법

# 이진 탐색트리
# 이진탬색의 개념을 트리 형태의 구조에 접목한 자료구조



