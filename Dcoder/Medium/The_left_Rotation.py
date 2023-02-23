from collections import deque
d = -int(input().split()[1])
arr = deque(map(int, input().split()))
arr.rotate(d)
print(' '.join(tuple(arr)))