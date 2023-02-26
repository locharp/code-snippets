for t in range(int(input())):
  n = int(input())
  ap = tuple(map(int, input().split()))
  d = (ap[-1] - ap[0]) // (n - 1)
  if ap[1] - ap[0] != d:
    if ap[2] - ap[1] == ap[1] - ap[0]:
      print(ap[-1])
    elif ap[2] - ap[1] == d:
      print(ap[0])
    else:
      print(ap[1])
  else:
    for i in range(2, n):
      if ap[i] - ap[i-1] != d:
        print(ap[i])
        break