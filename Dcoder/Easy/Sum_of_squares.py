a, b = map(int, input().split())
print(sum(i**2 for i in range(a, b + 1)))