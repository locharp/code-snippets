for t in range(int(input())):
  n, m = map(int, input().split())
  n += 1
  for i in range(n):
    print(m // n + (1 if m % n > i else 0), end=' ')
  print()