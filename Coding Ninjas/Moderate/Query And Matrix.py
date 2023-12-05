def query( mat, m, n, q ):
    
    r = [ 1 ] * m
    c = [ 0 ] * n
    ans = []

    for p in q:
        if "R" in p:
            t, s = p.split( "R" )
            s = int( s )

            if t == "1":
                r[s] = 1 - r[s]
            else:
                o = 0

                for i in range( n ):
                    o += abs( r[s] - c[i] )

                ans.append( o )
        else:
            t, s = p.split( "C" )
            s = int( s )

            if t == "1":
                c[s] = 1 - c[s]
            else:
                o = 0

                for i in range( m ):
                    o += abs( r[i] - c[s] )

                ans.append( o )

    return ans
