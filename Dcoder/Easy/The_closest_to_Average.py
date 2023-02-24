n = int(input())
a = sum(map(int, input().split())) / n
print(int(a) + 1 if a % 1 > 0.5 else int(a))