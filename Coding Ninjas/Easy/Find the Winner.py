from collections import Counter
from sortedcontainers import SortedSet

def getWinner( votes ):
    a = sorted( Counter( vote[0] for vote in votes ).items(), key = lambda x: -x[1] )
    n = a[0][1]
    s = SortedSet()
    i = 0

    while i < len( a ) and a[i][1] == n:
        s.add( a[i][0] )
        i += 1
    
    return [ s[0] ]
