class Solution:

    def __init__( self ):

        self.a = []


        
    def f( self, root ):
        
        if root is None:
            return
            
        self.a.append( root.val )
        self.f( root.left )
        self.f( root.right )


        
    def getMinimumDifference( self, root: Optional[TreeNode] ) -> int:
        
        self.f( root )
        self.a.sort()

        return min( self.a[i] - self.a[ i - 1 ] for i in range( 1, len( self.a ) ) )
