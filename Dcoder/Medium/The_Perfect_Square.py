for t in range(int(input())):
  n = int(input())
  p = int(n ** .5)
  q = p + 1
  print(p if n - p**2 < q**2 - n else q)