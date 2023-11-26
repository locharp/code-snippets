from collections import defaultdict

d = defaultdict( int )

for i in range( int( input() ) ):
    d[input()] += 1
    
print( len( d ) )
print( " ".join( [ str( j ) for j in d.values() ] ) )
