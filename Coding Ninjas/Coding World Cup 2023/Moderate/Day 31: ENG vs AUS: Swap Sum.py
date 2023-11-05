def swapSum( k: int, a: List[int], b: List[int] ) -> int:
    
    c = sorted( b[i] - a[i] for i in range( len( a ) ) )
    s = sum( max( i, 0 ) for i in c[ -k : ] )

    return sum( a ) + s
