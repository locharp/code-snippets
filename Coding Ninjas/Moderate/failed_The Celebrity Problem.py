# Time limit exceeded
from collections import *

def findCelebrity( n, knows ):
    u = { i for i in range( n ) }
    c = defaultdict( set )
    d = { i: { i } for i in range( n ) }

    for i in range( n ):
        for j in range( n ):
            if i == j:
                continue

            if knows( i, j ):
                c[i].add( j )
                d[j].add( i )

    for i in u - set( c ):
        for j in u - d[i]:
            if knows( j, i ):
                d[i].add( j )
            else:
                break

        if len( d[i] ) == n:
            return i

    return -1
