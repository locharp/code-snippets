from collections import defaultdict
from sortedcontainers import SortedSet

def nextGreater( S ):

    d = defaultdict( int )
    n = len( S )
    s = SortedSet()

    for i in range( n - 1, -1, -1 ):
        d[ S[i] ] += 1
        s.add( S[i] )

        for j in s:
            if j > S[i]:
                d[j] -= 1
                
                return S[ : i ] + j + "".join( [ k * d[k] for k in s ] )

    return "-1"
