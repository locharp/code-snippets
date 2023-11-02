class Solution:

    def __init__( self ):

        self.c = 0



    def f( self, root ):

        if root is None:
            return ( 0, 0 )

        p, q = self.f( root.left )
        r, s = self.f( root.right )
        u, v = p + r + 1, q + s + root.val

        if v // u == root.val:
            self.c += 1
        
        return ( u, v )



    def averageOfSubtree( self, root: Optional[TreeNode] ) -> int:
        
        self.f( root )

        return self.c
