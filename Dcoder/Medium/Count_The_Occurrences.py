input()
arr = input().split()
for q in range(int(input())):
  n = arr.count(input())
  print(n if n else -1)