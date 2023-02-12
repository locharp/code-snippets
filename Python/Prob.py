def fact(n):
  res = 1
  if n > 1:
    for i in range(2, n+1):
      res *= i
  return res

def nPr(n, r):
  res = 1
  if n > 1:
    for i in range(n, n-r, -1):
      res *= i
  return res

def nCr(n, r):
  return nPr(n,r) // fact(r)

def exact(n, r, p):
  return p**r * (1-p)**(n-r) * nCr(n, r)

def at_least(n, r, p):
  res = 0
  for k in range(r, n+1):
    res += exact(n, k, p)
  return res

def at_most(n, r, p):
  return 1 - at_least(n, r+1, p)

def a_or_b(a, b, ab, t):
  return (a + b - ab) / t, f"{a + b - ab}/{t}"