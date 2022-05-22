import sys
s, x = map(int, sys.stdin.readline().split())
a = list(map(int, input().split()))
for i in a:
    if x > i:
        print(i, end=' ')


