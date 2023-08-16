class Solution:
    def sortedArrayToBST( self, nums: List[int] ) -> Optional[TreeNode]:
        def f( p, a ):
            n = len( a )
            m = ( n + 1 ) // 2
            
            if n > 1:
                r = ( m + n ) // 2
                p.right = TreeNode( a[r] )
                f( p.right, a[ m : r ] + a[ r + 1 : ] )
                
            if n > 0:
                l = m // 2
                p.left = TreeNode( a[l] )
                f( p.left, a[ : l ] + a [ l + 1 : m ] )
                
        m = len( nums ) // 2
        root = TreeNode( nums[m] )
        f( root, nums[ : m ] + nums[ m + 1 : ] ) 
        
        return root