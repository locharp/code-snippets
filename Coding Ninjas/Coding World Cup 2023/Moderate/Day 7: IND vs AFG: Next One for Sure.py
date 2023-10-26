from math import ceil

def f( x, y, m, n, o ):
    
    if m == y:
        return n + m * o

    return f( x, y, m + 1,
     n + m * x * o / 100, o * ( 1 - x / 100 ) )



def nextOneForSure( x: int, y: int ) -> int:
    
    if x == 100:
        return 2

    return ceil( f( x, y, 1, 0, 1 ) * 2 )
