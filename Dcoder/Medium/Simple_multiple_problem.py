from math import gcd

for t in range( int( input() ) ):
    n, m = map( int, input().split() )
    print( m // gcd( n, m ) )