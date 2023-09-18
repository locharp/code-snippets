class Solution:
    def __init__( self ):
        self.ans = []
    
    def postorder( self, root: 'Node' ) -> List[int]:
        if root is not None:
            for child in root.children:
                self.postorder( child )
                
            self.ans.append( root.val )
                
        return self.ans