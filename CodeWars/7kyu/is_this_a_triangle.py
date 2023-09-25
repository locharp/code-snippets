def is_triangle( a, b, c ):
    m = max( a, b, c )
    n = min( a, b, c )
    o = a + b + c
    
    return n > 0 and m * 2 < o
