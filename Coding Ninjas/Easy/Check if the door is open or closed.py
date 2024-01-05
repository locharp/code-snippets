def doorStatus( n ):
    
    a = [ 1 ] * n

    for i in range( 2, n + 1 ):
        for j in range( i - 1, n, i ):
            a[j] = 1 - a[j]

    return "".join( map( str, a ) )
