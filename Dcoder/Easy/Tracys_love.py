a, b = map(int, input().split())
print('Love' if a + b == 6 or abs(a - b) == 6 else 'Hate')