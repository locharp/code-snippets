from itertools import *

def kthSmallest( arr, k ):
    
    if len( arr ) * ( len( arr ) - 1 ) // 2 < k:
        return -1
    
    return sorted( i * j for i, j in combinations( arr, 2 ) )[ k - 1 ]
