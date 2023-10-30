def isDeadEnd( root, m = 1, n = 10 ** 9 ):
    
    if root is None:
        return False
        
    if m == n or isDeadEnd( root.left, m, root.data - 1 ) or isDeadEnd( root.right, root.data + 1, n ):
        return True
        
    return False
    
    
    
def isDeadEnd2(root):
    
    q = [ ( root, 1, 10 ** 9 + 1 ) ]

    while len( q ) > 0:
        p, r, s = q.pop()
        if p.data == r and p.data == s:
            return True

        if p.left is not None:
            q.append( ( p.left, r, p.data - 1 ) )
        
        if p.right is not None:
            q.append( ( p.right, p.data + 1, s ) )

    return False
