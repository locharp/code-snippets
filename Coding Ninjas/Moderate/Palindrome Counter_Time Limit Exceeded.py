def countPalindromeSubstrings( s: str ):
    n = len( s )
    c = set()
    d = set()
    ans = 0

    for i in range( n ):
        for j in range( i + 1, n + 1 ):
            t = s[ i : j ]
            
            if t in c:
                ans += 1
            elif t in d:
                continue
            elif t == t[ : : -1 ]:
                ans += 1
                c.add( t )
            else:
                d.add( t )

    return ans
