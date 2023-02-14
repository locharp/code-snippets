from math import sqrt
for i in range(int(input())):
  m, n, o = map(int, input().split())
  s = (m + n + o) / 2
  print('True' if s * 2 == sqrt(s * (s-m) * (s-n) * (s-o)) else 'False')