a = [[1]]
n = int(input())
for i in range(1, n):
  a.append([1])
  for j in range((i-1) // 2):
    a[i] += [sum(a[i-1][j:j+2])]
  if i % 2 == 0:
    a[i] += [a[i-1][-1] * 2]
for i in range(n):
  print(' '*(n-i-1) + ' '.join(map(str, a[i][:i]+a[i][(i-1)//2::-1])))