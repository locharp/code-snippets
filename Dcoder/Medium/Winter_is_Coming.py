for t in range(int(input())):
  input()
  a = tuple(map(int, input().split()))
  print(max(sum(a[::2]), sum(a[1::2])))