from itertools import combinations

s, k = input().split()
s = sorted( s )
k = int( k )

for i in range( 1, k + 1 ):
    a = list( combinations( s, i ) )
    
    for j in a:
        print( "".join( j ) )
