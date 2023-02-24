from operator import mul
from functools import reduce
n = int(input())
print(reduce(mul, range(1, n+1)) // reduce(mul, range(1, n-1)) if n > 2 else n // 2)