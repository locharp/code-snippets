from itertools import combinations_with_replacement

s, k = input().split()
s = sorted( s )
k = int( k )

for i in combinations_with_replacement( s, k ):
    print( "".join( i ) )
