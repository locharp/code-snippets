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
        else:
            if j == 0:
                d[j].add( i )
            else:
                t = True
                o = ""

                for k in d[j]:
                    if i[j] == k[j]:
                        if len( i ) < len( k ):
                            o = k
                        else:
                            t = False

                        break
                        
                if t:
                    if o != "":
                        d[j].remove( o )

                    d[j].add( i )
                    
    return sorted( d[ max( d ) ] )
