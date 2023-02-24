for i in range(int(input())):
  n, m = map(int, input().split())
  print('No' if m % n else 'Yes')