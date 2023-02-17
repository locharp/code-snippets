for i in range(int(input())):
  s = input()
  if s[-3:] == 'est':
    print(s)
  elif s[-2:] == 'er':
    print(s[:-2] + 'est')
  else:
    print(s + ('r' if s[-1] == 'e' else 'er'))