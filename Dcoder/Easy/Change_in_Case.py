n = int(input())
s = list(input())
x, y = map(int, input().split())
for i in (x, y):
  s[i] = s[i].lower() if s[i].isupper() else s[i].upper()
print(''.join(s))