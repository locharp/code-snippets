from collections import *

def spellChecker( dictionary, query ):

    d = defaultdict( set )

    for i in dictionary:
        j = 0
        
        while j < len( query ):
            if j == len( i ) or i[j] != query[j]:
                break
            
            j += 1
        
        if j == len( query ) and j == len( i ):
            return [ "CORRECT" ]

        d[j].add( i )
        
    ans = sorted( d[ max( d ) ] )
    i = 1

    while i < len( ans ):
        if ans[ i - 1 ] == ans[i][ : len( ans[ i - 1 ] ) ]:
            ans.pop( i )
        else:
            i += 1

    return ans
