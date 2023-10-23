def planetMisery( n: int, m: int ) -> int:
    
    return n * 2 if n == m else min( m, n ) * 2 + 1
