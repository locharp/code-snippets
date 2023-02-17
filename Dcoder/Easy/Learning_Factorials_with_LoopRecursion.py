from functools import reduce
from operator import __mul__
print(reduce(__mul__, range(1, int(input())+1)))