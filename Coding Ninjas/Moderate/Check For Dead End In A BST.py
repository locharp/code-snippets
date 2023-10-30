def isDeadEnd(root):
    
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
