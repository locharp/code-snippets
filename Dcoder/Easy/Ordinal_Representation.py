n = int(input())
print(str(n) + ('st' if n == 1 else 'nd' if n < 3 else 'rd' if n == 3 else'th'))