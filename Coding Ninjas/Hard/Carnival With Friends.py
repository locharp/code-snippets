def carnivalRides( n, k, rides ):
    
    a = sorted( rides, key = lambda x: ( x[1], x[0] ) )
    g = []
    ans = 0

    for i, j in a:
        t = True

        for h in range( len( g ) - 1, -1, -1 ):
            if g[h] <= i:
                g.pop( h )
                g.append( j )
                ans += 1
                t = False
                break
        
        if t and len( g ) < k:
            g.append( j )
            ans += 1

    return ans
