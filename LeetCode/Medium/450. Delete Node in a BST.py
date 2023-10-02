class Solution:
    def deleteNode( self, root: Optional[TreeNode], key: int ) -> Optional[TreeNode]:
        if root is None:
            return root
        
        
        
        def f( root, c ):
            if c is None:
                return
            
            elif c.val > root.val:
                if root.right is None:
                    root.right = c
                else:
                    f( root.right, c )
            elif root.left is None:
                root.left = c
            else:
                f( root.left, c )
                
                
                
        p = temp = TreeNode( -106, None, root )
        curr = root
        
        while curr is not None:
            if curr.val == key:
                if curr == p.left:
                    p.left = None
                else:
                    p.right = None
            
                f( p, curr.left )
                f( p, curr.right )
                break
                
            p = curr
            
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right
        
        return temp.right
