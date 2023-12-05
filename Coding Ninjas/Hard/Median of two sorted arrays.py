def median( a: int, b: int ) -> float:
    
    n = len( a )
    m = len( b )
    o = n + m
    
    if o % 2 > 0:
        return float( sorted( a + b )[ o // 2 ] )
    else:
        return sum( sorted( a + b )[ o // 2 - 1: o // 2 + 1 ] ) / 2
