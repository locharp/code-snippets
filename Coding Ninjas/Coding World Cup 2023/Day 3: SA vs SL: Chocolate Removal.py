def totalChocolates( n: int, a: List[int] ) -> int:
    
    return sum( max( i - 23, 0 ) for i in a )
