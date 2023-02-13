for i in range(int(input())):
  m, a = map(int, input().split())
  print('Pass' if m > 70 and a > 50 else 'Fail')