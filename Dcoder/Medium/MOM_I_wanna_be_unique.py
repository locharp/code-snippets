from collections import Counter

n = int( input() )
arr = Counter( input().split() )

for p, q in arr.items():
    if q == 1:
        print( p )
        break