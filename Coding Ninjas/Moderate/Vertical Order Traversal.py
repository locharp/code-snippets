def f( d, p ):
    
    if len( p ) < 1:
        return d
        
    q = []
    
    for i, j in p:
        d[i].append( j.data )
        
        if j.left is not None:
            q.append( ( i - 1, j.left ) )
            
        if j.right is not None:
            q.append( ( i + 1, j.right ) )
            
    return f( d, q )
    
    
    
def verticalOrderTraversal( root ):
    
    d = f( defaultdict( list ), [ ( 0, root ) ] )
    
    return [ k for i in sorted( d ) for k in d[i] ]
