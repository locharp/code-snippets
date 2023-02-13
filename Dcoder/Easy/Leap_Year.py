for i in range(int(input())):
  year = int(input())
  print('Yes' if year % 400 == 0 or year % 100 and year % 4 == 0 else 'No')