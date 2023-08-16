class Solution:
    def levelOrder( self, root: Optional[TreeNode] ) -> List[List[int]]:
        def f( n, i ):
            if n is None:
                return
            
            if len( ans ) == i:
                ans.append( [] )
                
            ans[i].append( n.val )
            
            if n.left is not None:
                f( n.left, i + 1 )
                
            if n.right is not None:
                f( n.right, i + 1 )
        
        ans = []
        
        f( root, 0 )
        
        return ans