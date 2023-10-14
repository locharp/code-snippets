from itertools import product

def sqaure( s ):
    return pow( int( s ), 2 )
    
k, m = map( int, input().split() )
x = [ list( map( square, input().split() ) )[ 1 : ] for i in range( k ) ]
 
print( max( sum( i ) % m for i in product( *x ) ) )
