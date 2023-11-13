class Codec:

    def serialize( self, root ):
        
        if root is None:
            return ""
        
        a = [ str( root.val ) ]
        q = [ root ]
        
        while len( q ) > 0:
            p = []
            
            for i in q:
                if i.left is None:
                    a.append( "#" )
                else:
                    a.append( str( i.left.val ) )
                    p.append( i.left )
                    
                if i.right is None:
                    a.append( "#" )
                else:
                    a.append( str( i.right.val ) )
                    p.append( i.right )
                        
            q = p
            
        j = len( a ) - 1
        
        while a[j] == "#" and a[ j - 1 ] == "#":
            j -= 2
            
        return ",".join( i for i in a[ : j + 1 ] )
            
        
        
    def deserialize( self, data ):
        
        if data == "":
            return []
        
        a = data.split( "," )
        root = TreeNode( int( a[0] ) )
        q = [ root ]
        j = 1
        
        while len( q ) > 0:
            p = []
            
            for i in q:
                if j == len( a ):
                    break
                    
                if a[j] != "#":
                    i.left = TreeNode( int( a[j] ) )
                    p.append( i.left )
                    
                j += 1
                
                if a[j] != "#":
                    i.right = TreeNode( int( a[j] ) )
                    p.append( i.right )
                    
                j += 1
                
            q = p
            
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
