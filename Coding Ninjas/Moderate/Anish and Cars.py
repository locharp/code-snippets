from typing import *
from sortedcontainers import SortedList

def find( n: int, position: List[int], speed: List[int], d: int ) -> int:
    
    a = SortedList()
    
    for i in range( n ):
        a.add( [ position[i], speed[i] ] )
        
    a[-1][1] = ( d - a[-1][0] ) / a[-1][1]
    
    for i in range( n - 2, -1, -1 ):
        a[i][1] = max( a[ i + 1 ][1], ( d - a[i][0] ) / a[i][1] )
        
    s = { i[1] for i in a }
    
    return len( s )
