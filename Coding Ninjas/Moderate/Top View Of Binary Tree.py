def f( root, d, i, j ):

    if root is None:
        return
        
    if i not in d:
        d[i] = [ root.val, j ]
    elif j < d[i][1]:
        d[i] = [ root.val, j ]
        
    f( root.left, d, i - 1, j + 1 )
    f( root.right, d, i + 1, j + 1 )



def getTopView( root ):
    
    d = {}
    f( root, d, 0, 0 )
    
    return [ j[0] for i, j in sorted( d.items() ) ]
