from sortedcontainers import SortedSet

def kthSmallestLargest( arr,k ):
    
    s = SortedSet( arr )

    if k > len( s ):
        return [ -1, -1 ]
    else:
        return [ s[ k - 1 ], s[-k] ]
