for i in range(int(input())):
  s = bin(int(input()))[2:]
  print(int(s[1:] + s[0])