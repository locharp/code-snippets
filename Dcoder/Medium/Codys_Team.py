n, k = map(int, input().split())
marks = tuple(map(int, input().split()))
highest = 0
for i in range(n - k + 1):
  highest = max(highest, sum(marks[i:i+k]))
print(highest)