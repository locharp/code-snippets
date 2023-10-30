from collections import defaultdict

def countElements( x: int, a: List[int] ) -> int:
    
    d = defaultdict( int )
    i = 0

    while i < len( a ):
        if d[i] < x:
            d[i] += 1
            i += 1
        else:
            break

    return i
