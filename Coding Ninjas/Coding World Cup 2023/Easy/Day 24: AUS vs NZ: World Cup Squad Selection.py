def rejection( n: int, a: List[int], b: List[int] ) -> int:
    
    return sum( a ) + max( b[i] - a[i] for i in range( n ) )
