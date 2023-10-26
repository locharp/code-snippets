def f( a, i ):

    if a[i] == 1:
        return 1
    else:
        return 1 + f( a, a[i] - 2 )
    
    
    
def calculateDistance( n: int, a: list ) -> int:
    
    return f( a, -1 )
