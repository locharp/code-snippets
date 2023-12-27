from bisect import bisect_left

def f( a, root ):

    if root == None:
        return
        
    f( a, root.left )
    a.append( root.data )
    f( a, root.right )

    

def predecessorSuccessor( root, key ):
    
    a = []
    f( a, root )
    i = bisect_left( a, key )
    ans = [ -1, -1 ]

    if i > 0:
        ans[0] = a[ i - 1 ]
        
    if i < len( a ):
        if a[i] > key:
            ans[1] = a[i]
        else:
            ans[1] = a[ i + 1 ]

    return ans
