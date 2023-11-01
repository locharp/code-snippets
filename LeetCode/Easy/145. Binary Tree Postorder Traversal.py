class Solution:
    
    def __init__( self ):
        
        self.a = []
        
        
        
    def postorderTraversal( self, root: Optional[TreeNode] ) -> List[int]:
        
        if root is None:
            return
        
        self.postorderTraversal( root.left )
        self.postorderTraversal( root.right )
        self.a.append( root.val )
        
        return self.a
