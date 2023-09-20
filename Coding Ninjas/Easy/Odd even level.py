def evenOddLevelDifference( root ): 
    if root is None:
        return 0
    
    ans = [ 0, 0 ]
    i = 0
    p = [ root ]
     
    while len( p ) > 0:
        q = p
        p = []
        
        for n in q:
            ans[i] = ( ans[i] + n.data )
            
            if n.left is not None:
                p.append( n.left )
                
            if n.right is not None:
                p.append( n.right )
                
        i = ( i + 1 ) % 2
        
    return abs( ans[0] - ans[1] )