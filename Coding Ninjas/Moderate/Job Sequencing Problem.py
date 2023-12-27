from sortedcontainers import SortedList

def jobScheduling( jobs ):

    jobs = sorted( ( j, k ) for i, j, k in jobs )
    a = SortedList()
    
    for i, j in jobs:
        if i > len( a ):
            a.add( j )
        elif j > a[0]:
            a.pop( 0 )
            a.add( j )

    return [ len( a ), sum( a ) ]
