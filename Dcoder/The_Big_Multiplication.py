from functools import reduce
input()
print(reduce(lambda i, j: i * j % 1000000007, map(int, input().split())))