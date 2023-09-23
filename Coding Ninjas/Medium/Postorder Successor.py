def postOrderSuccessor( root, m ):
    if root == None:
        return 0
        
    if root.val == m:
        return -1
        
    def f( root, m, t ):
        if root is None:
            return -1
        elif root.val == m:
            return 0
        
        n = f( root.left, m, t )
        
        if n == 0:
            if root.right is not None:
                return f( root.right, m, True )
            else:
                return root.val
        elif n > 0:
            return n
    
        n = f( root.right, m, t )
        
        if n == 0:
            return root.val
        elif n > 0:
            return n
        
        if t:
            return root.val
        else:
            return n
       
    ans = f( root, m, False )
    
    if ans == 0:
        return root.val
    else:
        return ans
