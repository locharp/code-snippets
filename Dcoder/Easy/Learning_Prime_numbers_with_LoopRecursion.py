m, n = map(int, input().split())
if m < 3:
  print(2)
for i in range(max(m, 3), n+1, 2):
  for j in range(3, int(i**.5)+1):
    if i % j == 0:
      break
  else:
    print(i)