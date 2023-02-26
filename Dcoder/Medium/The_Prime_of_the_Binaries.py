num = int(input(), 2)
print(num)
if num < 4:
  print('Not', end=' ')
else:
  for i in range(2, int(num**.5) + 1):
    if num % i == 0:
      print('Not', end=' ')
      break
print('Prime')