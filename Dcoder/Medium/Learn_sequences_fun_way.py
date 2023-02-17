n = int(input())
s = tuple(map(int, input().split()))
i, j = 1, len(s) - 1
while i < j - 1 and s[i] < s[i-1]:
  i += 1
while i < j and s[i] < s[i+1]:
  i += 1
print('Yes' if i == j else 'No')