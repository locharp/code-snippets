input()
a = tuple(map(int, input().split()))
for i in a:
  for j in range(1, 14):
    if j**j == i:
      print('Yes', end=' ')
      break
  else:
    print('No', end=' ')