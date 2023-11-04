from sortedcontainers import SortedList

def nextGreater( S ):

    a = SortedList()
    n = len( S )

    for i in range( n - 1, -1, -1 ):
        for j in a:
            if j > S[i]:
                a.remove( j )
                a.add( S[i] )

                return S[ : i ] + j + "".join( a )

        a.add( S[i] )

    return "-1"
