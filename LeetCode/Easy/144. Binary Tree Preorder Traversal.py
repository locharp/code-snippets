class Solution:
    
    def __init__( self ):
        
        self.a = []
        
        
        
    def preorderTraversal( self, root: Optional[TreeNode] ) -> List[int]:
        
        if root is None:
            return
        
        self.a.append( root.val )
        self.preorderTraversal( root.left )
        self.preorderTraversal( root.right )
        
        return self.a
