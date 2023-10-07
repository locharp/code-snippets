def balancedParantheses( n, a = [ [], [ "()" ] ] ):
    
    if len( a ) > n:
        return a[n]
    
    s = set()
    
    for p in balancedParantheses( n - 1, a ):
        s.update( { "()" + p, "(" + p + ")", p + "()" } )
            
    for i in range( 2, n // 2 + 1 ):
        for p in balancedParantheses ( i, a ):
            for q in balancedParantheses( n - i, a ):
                s.update( { p + q, q + p } )
                
    a.append( list ( s ) )
    
    return a[n]
