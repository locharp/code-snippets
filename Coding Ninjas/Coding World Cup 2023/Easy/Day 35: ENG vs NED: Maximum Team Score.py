def maximumAggregateCount( n: int, a: List[int] ) -> int:
    
    if n < 2:
        return 0
        
    return sum( a ) - min( a[0], a[-1] )
