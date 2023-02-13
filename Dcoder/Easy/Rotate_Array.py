from collections import deque

k = int(input().split()[1])
a = deque(input().split())
a.rotate(k)
print(' '.join(a))