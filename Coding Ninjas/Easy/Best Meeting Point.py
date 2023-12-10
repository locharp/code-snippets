def findBestMeetingPoint( mat ):
    
    p = []
    q = []
    
    for i in range( len( mat ) ):
        for j in range( len( mat[0] ) ):
            if mat[i][j] > 0:
                p.append( i )
                q.append( j )

    p.sort()
    q.sort()
    o = len( p ) // 2
    x = y = 0
    
    if len( p ) % 2 > 0:
        x = p[o]
        y = q[o]
    else:
        x = sum( p[ o - 1 : o + 1 ] ) // 2
        y = sum( q[ o - 1 : o + 1 ] ) // 2

    ans = sum( abs( p[i] - x ) + abs( q[i] - y ) for i in range( len( p ) ) )

    return ans
