class Solution:
    def isSymmetric( self, root: Optional[TreeNode] ) -> bool:
        def f( l, r ):
            if l is None:
                return r is None
            elif r is None or l.val != r.val:
                return False
            
            return f( l.left, r.right ) and f( l.right, r.left )
        
        return f( root.left, root.right )