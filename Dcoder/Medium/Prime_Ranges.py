l, r = map(int, input().split())
for i in range(max(2, l), r+1):
  for j in range(2, int(i**.5)+1):
    if i % j == 0:
      break
  else:
    print(i, end=' ')