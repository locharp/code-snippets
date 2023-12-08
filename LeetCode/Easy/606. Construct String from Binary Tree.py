class Solution:

    def f( self, arr, root ):

        arr.append( "(" )
        arr.append( str( root.val ) )
        
        if root.left != None:
            self.f( arr, root.left )
        elif root.right != None:
            arr.append( "()" )
        
        if root.right != None:
            self.f( arr, root.right )

        arr.append( ")" )



    def tree2str( self, root: Optional[TreeNode] ) -> str:

        ans = []
        self.f( ans, root )

        return "".join( ans[ 1 : -1 ] )
