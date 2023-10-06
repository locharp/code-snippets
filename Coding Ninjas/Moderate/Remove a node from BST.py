def f( g, h ):
    if h == None:
        return
    
    i = j = g
    r = True
    
    while i != None:
        j = i
        
        if i.val < h.val:
            i = i.right
            r = True
        else:
            i = i.left
            r = False
            
    if r:
        j.right = h
    else:
        j.left = h

def removeNode( root, X ):
    if root.val == X:
        if root.right != None:
            if root.left != None:
                f( root.right, root.left )
                
            return root.right
        else:
            return root.left
    
    prev = head = root
    r = True
    
    while root.val != X:
        prev = root
        
        if root.val < X:
            root = root.right
            r = True
        else:
            root = root.left
            r = False
                            
    if r:
        prev.right = root.right
        f( prev, root.left )
    else:
        prev.left = root.left
        f( prev, root.right )
        
    return head