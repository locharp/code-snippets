class Solution:
    def isValidBST( self, root: Optional[TreeNode] ) -> bool:
        def f( r, p, q ):
            if r is None:
                return True
        
            if r.left is None:
                if r.right is None:
                    return True
                else:
                    return q > r.right.val > r.val and f( r.right, r.val, q )
            elif r.right is None:
                return r.val > r.left.val > p and f( r.left, p, r.val )
            else:
                return r.val > r.left.val > p and q > r.right.val > r.val and f( r.left, p, r.val ) and f( r.right, r.val, q )
        
        return f( root, -2 ** 31 - 1, 2 ** 31 )