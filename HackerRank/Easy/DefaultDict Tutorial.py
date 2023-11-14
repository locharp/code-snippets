from collections import defaultdict

p, q = map( int, input().split() )
a = defaultdict( list )

for i in range( 1, p + 1 ):
    a[ input() ].append( str( i ) )
    
for i in range( q ):
    o = input()
    
    if o in a:
        print( " ".join( a[o] ) )
    else:
        print( -1 )
