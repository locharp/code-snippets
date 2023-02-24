d = '0123456789'
for i in range(int(input())):
  n, s = input().split()
  n = int(n)
  for c in s:
    if c.isdigit():
      n -= 1
  print(n)
  if n == len(s):
    print('String')
  elif n == 0:
    print('Number')
  else:
    print('Variable')