m = sum(map(int, input().split())) / 3
if m > 90:
  print('A')
elif m > 80:
  print('B')
elif m > 70:
  print('C')
elif m > 60:
  print('D')
else:
  print('F')