class Solution:
    def isBalanced( self, root: Optional[TreeNode] ) -> bool:
        if root is None or root.left is None and root.right is None:
            return True
        
        return abs( self.get_height( root.left, 1 ) - self.get_height( root.right, 1 ) ) < 2 and self.isBalanced( root.left ) and self.isBalanced( root.right )
    
    def get_height( self, root, height ):
        if root is None:
            return height
        
        return max( self.get_height( root.left, height + 1), self.get_height( root.right, height + 1 ) )