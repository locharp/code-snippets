def f( root, a ):

    if root is None:
        return
    
    f( root.left, a )
    a.append( root.data )
    f( root.right, a)



def inorderSuccesor( root, node ):
    
    a = []
    f( root, a )
    
    for i in range( len( a ) ):
        if a[i] == node:
            if i + 1 < len( a ):
                return a[ i + 1 ]
