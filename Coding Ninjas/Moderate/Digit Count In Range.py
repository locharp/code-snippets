def f( n, s, t, a ):
    
    m = len( s ) - 1
    ans = 1 if s[-1] >= t else 0
    
    for i in range( m ):
        if s[i] > t:
            ans += 10 ** ( m - i )
        elif s[i] == t:
            ans += n % 10 ** ( m - i ) + 1
            
        if t < "1":
            ans -= 10 ** ( m - i )

        ans += int( s[i] ) * a[ m - i ]

    return ans



def digitCount(K, A, B):

    r = str( A )
    s = str( B )
    t = str( K )
    a = [ 0 ] * len( s )

    for i in range( len( s ) - 1 ):
        a[ i + 1 ] = a[i] * 10 + 10 ** i

    return f( B, s, t, a ) - f( A, r, t, a ) + r.count( t )
