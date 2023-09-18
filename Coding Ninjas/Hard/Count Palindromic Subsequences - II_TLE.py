def countPalinSubseq( s: str ) -> int:
    n = len( s )
    
    if n == 1:
        return 1
    
    ans = len( set( s ) )
    p = { s }
    r = { s }
    
    while n > 2:
        q = r
        r = set()
        
        while len( q ) > 0:
            m = q.pop()
            
            for i in range( len( m ) ):
                r.add( m[ : i ] + m[ i + 1 : ] )
                
        p.update( r )
        n -= 1
                
    for i in p:
        if i == i[ : : -1 ]:
            ans += 1
            
    return ans % 1000000007