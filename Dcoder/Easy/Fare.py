a, m, n, d = map(int, input().split())
print(min(a, d) * m + max(d - a, 0) * n)