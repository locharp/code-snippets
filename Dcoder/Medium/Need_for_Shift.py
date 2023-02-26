s = input()
d = int(input())
for ch in s:
  print(chr((ord(ch) - d - 97) % 26 + 97), end='')