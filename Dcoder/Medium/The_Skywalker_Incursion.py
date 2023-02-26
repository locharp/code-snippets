n = int(input())
if n < 2:
  print(2)
else:
  p, q = 1, 3
  while n >= q:
    p, q = q, q + p
  print(q)