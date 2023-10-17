from collections import Counter

def countPalindromeSubstrings( s: str ):
    n = len( s )
    a = Counter( s[ i : j ] for i in range( n ) for j in range( i + 1, n + 1 ) )

    return sum( a[i] for i in a if i == i[ : : -1 ] )
