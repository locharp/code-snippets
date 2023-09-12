def kSmallest(n, m, k, mat):
    u = mat.pop()
    
    for o in mat:
        v = []
        
        for p in o:
            for q in u:
                v.append( p + q )
                
        u = sorted( v )[ : k ]
        
    return sorted( u )[ k - 1 ]