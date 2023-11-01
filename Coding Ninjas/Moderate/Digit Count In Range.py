def f( a, n, s, t ):
    
    m = len( s ) - 1
    ans = 1 if s[-1] >= t else 0

    for i in range( m ):
        if s[i] > t and t > "0":
            ans += 10 ** ( m - i )
        elif s[i] == t:
            ans += n % 10 ** ( m - i ) + 1

        ans += int( s[i] ) * a[ m - i ]

    return ans



def digitCount(K, A, B):

    r = str( A - 1 )
    s = str( B )
    t = str( K )
    a = [ 0 ] * len( s )

    for i in range( len( s ) - 1 ):
        a[ i + 1 ] = a[i] * 10 + 10 ** i
    
    return f( a, B, s, t ) -f( a, A - 1, r, t )
