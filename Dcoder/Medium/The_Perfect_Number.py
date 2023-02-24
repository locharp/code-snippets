for t in range(int(input())):
  print(' '.join(tuple(map(lambda n: 'True' if int(n) in (6, 28, 496, 8128, 33550336) else 'False', input().split()))))