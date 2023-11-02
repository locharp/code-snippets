from collections import Counter

input()
arr = Counter( map( int, input().split() ) )
A = set( map( int, input().split() ) )
B = set( map( int, input().split() ) )
h = sum( j for i, j in arr.items() if i in A )
h -= sum( j for i, j in arr.items() if i in B )

print( h )
