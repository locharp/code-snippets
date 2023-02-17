a, b = map(int, input().split())
s = a + b
if s > 21 and 11 in (a, b):
    s -= 10
print(s if s < 22 else 0)