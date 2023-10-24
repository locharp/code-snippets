class Solution:

    def __init__( self ):

        self.a = []



    def largestValues( self, root: Optional[TreeNode], i = 0 ) -> List[int]:
        
        if root is None:
            return
        elif i >= len( self.a ):
            self.a.append( root.val )
        else:
            self.a[i] = max( self.a[i], root.val )
            
        self.largestValues( root.left, i + 1 )
        self.largestValues( root.right, i + 1 )

        return self.a
