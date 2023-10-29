from collections import *

def searchWords( booklet, diary ):

    d = defaultdict( list )
    ans = []

    for i in range( len( booklet ) ):
        for j in range( i + 1, len( booklet ) + 1 ):
            d[ booklet[ i : j ] ].append( i )

    for i in diary:
        ans += d[i]

    return sorted( ans )
