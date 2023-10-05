class Solution:
    def insertIntoBST( self, root: Optional[TreeNode], val: int ) -> Optional[TreeNode]:
        if root is None:
            return TreeNode( val )
        
        pev = curr = root
        
        while curr is not None:
            prev = curr

            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
                
        if prev.val > val:
            prev.left = TreeNode( val )
        else:
            prev.right = TreeNode( val )
        
        return root
