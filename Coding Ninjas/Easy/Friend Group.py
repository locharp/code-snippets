def friendGroup( n: int, a: List[int] ) -> int:
    
    m = sum( i % 2 for i in a )

    return max( m, n - m )
