a, b, p, q, x = map(int, input().split())
print(a&b, a|b, a^b, p<<q, p>>q, ~x, sep='\n')