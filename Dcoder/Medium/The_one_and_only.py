input()
a = tuple(map(int, input().split()))
for i in a:
  if a.count(i) == 1:
    print(i)
    break