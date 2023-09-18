class BSTIterator:

    def __init__( self, root: Optional[TreeNode] ):
        self.a = []
        curr = root
        
        while curr is not None:
            self.a.append( curr )
            curr = curr.left

    def next( self ) -> int:
        n = self.a.pop()
        curr = n.right
        
        while curr is not None:
            self.a.append( curr )
            curr = curr.left
            
        return n.val

    def hasNext( self ) -> bool:
        return len( self.a ) > 0