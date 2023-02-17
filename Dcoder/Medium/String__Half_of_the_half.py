for i in range(int(input())):
  s = input()
  for j in range(0, len(s) // 2, 2):
    print(s[j], end='')
  print()