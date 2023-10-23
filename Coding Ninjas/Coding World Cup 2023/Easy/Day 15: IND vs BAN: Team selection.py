def maxDifference( m: int, a: list ) -> int:
    
    a.sort()

    return sum( a[ -m : ] ) - sum( a[ : m ] )
