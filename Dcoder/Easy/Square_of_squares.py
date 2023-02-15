i = int(input())
if i < 0:
  print('NO')
else:
  print('YES' if int(i**.5)**2 == i else 'NO')