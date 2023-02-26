from math import factorial as f
n = input()
s = sorted(n, reverse=True)
l = len(n)
greater = 0
for i in range(l - 1):
  for j in range(l):
    if s[j] == n[i]:
      break
    greater += f(l - i - 1)
print(greater)