class Solution:
    def __init__( self ):
        self.ans = []
    def inorderTraversal( self, root: Optional[TreeNode] ) -> List[int]:
        if root is None:
            return
        
        self.inorderTraversal( root.left )
        self.ans.append( root.val )
        self.inorderTraversal( root.right )
        
        return self.ans
