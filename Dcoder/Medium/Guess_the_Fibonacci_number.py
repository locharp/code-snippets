def f(m, n, o):
  a = m + n
  if a > o:
    return a
  return f(n, a, o)

for i in range(int(input())):
  print(f(1, 1, int(input())))