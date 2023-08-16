class Solution:
    def maxDepth( self, root: Optional[TreeNode] ) -> int:
        if root is None:
            return 0
        
        def f( root, d ):
            if root.left is None:
                if root.right is None:
                    return d
                else:
                    return f( root.right, d + 1 )
            elif root.right is None:
                return f( root.left, d + 1 )
            else:
                return max( f( root.left, d + 1 ), f( root.right, d + 1 ) )
            
        return f( root, 1 )