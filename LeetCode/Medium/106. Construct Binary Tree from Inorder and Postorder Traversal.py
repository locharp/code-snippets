class Solution:
    
    def buildTree( self, inorder: List[int], postorder: List[int] ) -> Optional[TreeNode]:
        
        if len( inorder ) < 1:
            return None
        
        o = inorder.index( postorder[-1] )
        
        return TreeNode( inorder[o], self.buildTree( inorder[ : o ], postorder[ : o ] ), self.buildTree( inorder[ o + 1 : ], postorder[ o : -1 ] ) )
