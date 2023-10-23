from typing import List
from sortedcontainers import SortedList

def productionHouse( n: int, m: int, days: List[int], needs: List[int] ) -> int:

    a = SortedList( zip( days, needs ) )
    a.add( ( 0, 0 ) )
    c = 0

    for i in range( 1, len( a ) ):
        c += n * ( a[i][0] - a[ i - 1 ][0] ) - a[i][1]

        if c < 0:
            return 0
    
    return 1
