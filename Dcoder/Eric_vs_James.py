from math import gcd
def lcm(m, n):
  return m * n // gcd(m, n)
a, b = map(int, input().split())
m = 1
for i in range(a, b+1):
  m = lcm(m, i)
print(m)