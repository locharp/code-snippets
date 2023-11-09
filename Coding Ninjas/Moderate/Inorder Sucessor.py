def inorderSuccesor( root, node ):
    
    if root is None:
        return node
    
    if root.data == node:
        if root.right is None:
            return None
        else:
            return root.right.data
        
    ans = inorderSuccesor( root.left, node )
    
    if ans is None:
        return root.data
    elif ans != node:
        return ans

    return inorderSuccesor( root.right, node )
