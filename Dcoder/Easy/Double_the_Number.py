for i in range(int(input())):
  k = int(input().split()[1])
  a = list(map(lambda x: int(x) * 2, input().split()))
  print(a.count(k))