a, b = map(lambda s: int(s, 2), input().split())
print(bin(a + b)[2:])
print(bin(a * b)[2:])