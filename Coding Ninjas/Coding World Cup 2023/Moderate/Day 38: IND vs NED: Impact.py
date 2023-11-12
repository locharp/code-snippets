def subarray( n: int, x: List[int] ) -> int:
    
    return sum( x[i] * ( i + 1 ) for i in range( n ) )
