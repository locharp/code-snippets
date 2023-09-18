class Solution:
    def __init__( self ):
        self.ans = []
    
    def preorder( self, root: 'Node' ) -> List[int]:
        if root is not None:
            self.ans.append( root.val )
            
            for child in root.children:
                self.preorder( child )
            
        return self.ans