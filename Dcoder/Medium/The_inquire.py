input()
p = tuple(map(int, input().split()))
for i in range(int(input())):
  a, b = map(int, input().split())
  print(sum(p[a-1:b]))