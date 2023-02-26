d = {}
for n in range(int(input())):
  k, v = input().split()
  d[k] = v
for q in range(int(input())):
  print(d[input()])