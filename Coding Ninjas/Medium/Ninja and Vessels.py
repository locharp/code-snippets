def ninjaAndVessels(m, n, w):
    if w == m or w == n:
        return 1
    
    if m < n:
        m, n = n, m
        
    ans = []
    
    if w % n == 0:
        ans.append( w // n * 2 )
        
    for i in range( 1, n ):
        if ( m * i - w ) % n == 0:
            ans.append( ( ( ( ( m * i ) - w ) // n ) + i - 1 ) * 2 )
            
    for i in range( 1, m ):
        if ( n * i - w ) % m == 0:
            ans.append( ( ( ( ( n * i ) - n ) // m ) + i ) * 2 )
    
    if len( ans ) > 0:
        return min( ans )
    else:
        return -1