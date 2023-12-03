def similarStrings( n, a, b, c ):
    ans = [ 0, 2147483647 ]

    x = [ ord( i ) for i in a ]
    y = [ ord( i ) for i in b ]
    z = [ ord( i ) for i in c ]

    for i in range( n ):
        curr = 0

        for j in range( n ):
            k = ( i + j ) % n
            curr += abs( x[k] - y[j] ) + abs( x[k] - z[j] )

        ans[0] = max( ans[0], curr )
        ans[1] = min( ans[1], curr )

    return ans
