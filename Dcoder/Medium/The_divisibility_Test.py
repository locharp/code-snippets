for i in range(int(input())):
  n, x, y = map(int, input().split())
  for j in range(x, n, x):
    if j % y != 0:
      print(j, end=' ')
  print()