for i in range(int(input())):
  s = input()
  print('True' if any(c.islower() for c in s) and any(c.isupper() for c in s) and any(c.isdigit() for c in s) else 'False')