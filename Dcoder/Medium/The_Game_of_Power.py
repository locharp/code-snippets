def special(n):
  if n in range(8):
    return True if n in (1, 4) else False
  for i in range(2, int(n**.5) + 1):
    j = i * i
    while j <= n:
      if j == n:            
        return True
      j *= i        
  return False

def nearest(n):
  for i in range(n):
    if special(n-i) or special(n+i):
      return i

for t in range(int(input())):
  print(nearest(int(input())))