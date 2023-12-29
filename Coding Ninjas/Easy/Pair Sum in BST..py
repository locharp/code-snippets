def f( s, root ):

    if root == None:
        return

    f( s, root.left )
    s.add( root.data )
    f( s, root.right )



def pairSumBST( root, k ):
    
    s = set()
    f( s, root )

    for i in s:
        j = k - i

        if i != j and j in s:
            return True

    return False
