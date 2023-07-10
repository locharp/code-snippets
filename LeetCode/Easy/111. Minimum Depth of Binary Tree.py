class Solution:
    def minDepth( self, root: Optional[TreeNode], n : int = 0 ) -> int:
        if root is None:
            return n
        
        n += 1
        
        if root.left is root.right is None:
            return n
            
        if root.left is not None:
            left = self.minDepth( root.left, n )
        else:
            left = int( 1e6 )
            
        if root.right is not None:
            right = self.minDepth( root.right, n )
        else:
            right = int( 1e6 )
            
        return min( left, right )