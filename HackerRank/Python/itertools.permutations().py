from itertools import permutations

s, k = input().split()

for i in permutations( sorted( s ), int( k ) ):
    print( "".join( i ) )
