class Solution:
    def __init__( self ):
        self.ans = []
        
    def levelOrder( self, root: 'Node', i = 0 ) -> List[ List[int] ]:
        if root is not None:
            if i == len( self.ans ):
                self.ans.append( [] )
                
            self.ans[i].append( root.val )
            i += 1
            
            for child in root.children:
                self.levelOrder( child, i )
                
        return self.ans