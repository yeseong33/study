# def fac(n):
#     if n > 1:
#         return fac(n-1) * n
#     else:
#         return 1
#
#
# print(fac(10))
#
# def fac(n):
#     def loop(n, k):
#         if n > 1:
#             return loop(n-1,k * n)
#         else:
#             return k
#     return loop(n, 1)
#
# print(fac(10))
#
#
#
#
# def fi(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return fi(n-1) + fi(n-2)
#
#
# def power(x,n):
#     if n == 0:
#         return 1
#     elif n % 2 == 0:
#         return power(x*x, n//2)
#     else:
#         return x * power(x*x, (n-1)//2)


# print(power(2,9))
# 시간복잡도
# 순환 함수 = 0(log2(n))
# 반복 함수 = 0(n)

# 피보나치 수열 반복으로 하는 경우
# def fib_iter(n):
#     if n < 2:
#         return n
#     last = 0
#     current = 1
#     for i in range(2, n+1):
#         current, last = current + last, current
#     return current
#
#
# print(fib_iter(8))
# 시간 복잡도 0(n)


# 피보나치 수열 순환으로 하는 경우
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# print(fib(8))
# 시간복잡도 0(n ** 2)


#하노이탑
# def hanoi_tower(n, fr, tmp, to):
#     if n == 1:
#         print("원판 1: %s --> %s" % (fr, to))
#     else:
#         hanoi_tower(n-1, fr, to, tmp)
#         print('원판 %d: %s --> %s'%(n, fr, to))
#         hanoi_tower(n-1, tmp, fr, to)
#
#
# hanoi_tower(2,'a','b','c')


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
    # 괄호개수 확인 n = 0
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                return False
        else:
            left = stack.pop()
            if

