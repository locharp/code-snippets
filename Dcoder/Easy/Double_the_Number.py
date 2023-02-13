t = int(input())

for i in range(t):
  k = int(input().split()[1])
  a = list(map(lambda x: int(x) * 2, input().split()))
  print(a.count(k))