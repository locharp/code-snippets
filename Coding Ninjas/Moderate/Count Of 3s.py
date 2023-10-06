def countOf3( x ):
    s = str( x )
    m = len( s ) - 1
    a = [ 0 ] * ( m + 1 )
    ans = 1 if x % 10 >= 3 else 0
    
    for i in range( m ):
        a[ i + 1 ] = a[i] * 10 + 10 ** i
        
    for i in range( m ):
        if s[i] > "3":
            ans += 10 * a[ m - i ]
        elif s[i] == "3":
            ans += x % 10 ** ( m - i ) + 1
            
        ans += int( s[i] ) * a[ m - i ]
        
    return ans
