def reverseLevelOrder( root ):
    
    if root == None:
        return []
    
    a = []
    q = [ root ]
    
    while len( q ) > 0:
        p = []
        
        for i in q:
            a.append( i.val )
            
            if i.left != None:
                p.append( i.left )
                
            if i.right != None:
                p.append( i.right )
                
        q = p
        
    return a[ : : -1 ]
