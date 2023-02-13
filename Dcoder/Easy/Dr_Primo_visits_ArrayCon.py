input()
arr = map(int, input().split())
c = 0
for a in arr:
  if a == 1:
    cntinue
  for i in range(2, int(a**.5) + 1):
    if a % i == 0:
      break
  else:
    c += 1
print(c)