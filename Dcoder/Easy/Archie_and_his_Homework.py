from math import gcd
x, y = map(int, input().split())
d = gcd(x, y)
print(x//d, y//d)