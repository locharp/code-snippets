from collections import *

def smallestWindow( s, x ):
    
    c = Counter( x )
    d = defaultdict( list )
    u = v = 0
    t = len( x ) - 1

    while s[u] not in c:
        u += 1

    v = u
    c[ s[u] ] -= 1

    while t > 0:
        v += 1

        if s[v] in c:
            if c[ s[v] ] > 0:
                t -= 1
                
            c[ s[v] ] -= 1

    while c[ s[u] ] < 0:
        c[ s[u] ] += 1
        u += 1
        
        while s[u] not in c:
            u += 1

    v -= u
    t = u
    
    for i in range( u + v + 1, len( s ) ):
        if s[i] in c:
            c[ s[i] ] -= 1

            while c[ s[t] ] < 0:
                c[ s[t] ] += 1
                t += 1
                
                while s[t] not in c:
                    t += 1

            if v > i - t:
                u = t
                v = i - t

    return s[ u : u + v + 1 ]
