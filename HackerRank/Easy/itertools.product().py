from itertools import product

print ( " ".join( str( i ) for i in product( map( int, input().split() ), map( int, input().split() ) ) ) )
