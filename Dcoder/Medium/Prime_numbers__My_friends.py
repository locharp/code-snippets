from primePy import primes
p = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 61, 67, 71, 73, 79, 83, 93, 97)
n = int(input())
i = 0
while i < len(p):
  j = i + 1
  while j < len(p):
    if p[i] + p[j] == n:
      print(p[i], p[j])
    j += 1
  i += 1