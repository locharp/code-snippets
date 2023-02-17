for i in range(int(input())):
  s = ['', '']
  st = input()
  for i in range(len(st)):
    s[i%2] += st[i]
  print(s[0], s[1])