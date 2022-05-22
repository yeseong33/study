import sys

# (1)
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break

# (2)
for i in sys.stdin:
    a, b = map(int, i.split())
    print(a, b)