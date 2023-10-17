def countPalindromeSubstrings( s: str ):
    n = len( s )
    c = {}
    d = set()

    for i in range( n ):
        for j in range( i + 1, n + 1 ):
            t = s[ i : j ]
            
            if t in c:
                c[t] += 1
            elif t in d:
                continue
            elif t == t[ : : -1 ]:
                c[t] = 1
            else:
                d.add( t )

    return sum( c.values() )
