class Solution:
    def isSameTree( self, p: Optional[TreeNode], q: Optional[TreeNode] ) -> bool:
        if p is None:
            return q is None
        elif q is None:
            return False
        
        if p.val != q.val:
            return False
            
        return self.isSameTree( p.left, q.left ) and self.isSameTree( p.right, q.right )
