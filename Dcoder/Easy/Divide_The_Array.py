n = int(input())
a = tuple(map(int, input().split()))
for i in range(1, n, 2):
  if a[i] % 2 == 0:
    print(a[i], end=' ')