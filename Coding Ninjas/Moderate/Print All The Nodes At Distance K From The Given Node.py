def f( root, a, i ):
    
    if root is None:
        return
    elif i >= len( a ):
        a.append( [] )
    
    a[i].append( root.data )
    f( root.left, a, i + 1 )
    f( root.right, a, i + 1 )
    


def kDistance( root, target, k ):

    p = []
    q = []
    f( root.left, p, 0 )
    f( root.right, q, 0 )
    a = p[ : : -1 ] + [ [ root.data ] ] + q
    ans = []

    for i in range( len( a ) ):
        if target in a[i]:
            if i + k < len( a ):
                ans += a[ i + k ]
                
            if i - k >= 0:
                ans += a[ i - k ]
                
            break

    return ans
