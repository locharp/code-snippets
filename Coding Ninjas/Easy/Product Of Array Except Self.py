def getProductArrayExceptSelf( arr, n ):
    
    p = [ 1 ] * n
    q = [ 1 ] * n
    m = 1000000007

    for i in range( 1, n ):
        p[i] = p[ i - 1 ] * arr[ i - 1 ] % m

    for i in range( n - 1, 0, -1 ):
        q[ i - 1 ] = q[i] * arr[i] % m

    return [ p[i] * q[i] % m for i in range( n ) ]
