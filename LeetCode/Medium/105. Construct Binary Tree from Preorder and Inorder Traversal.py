class Solution:
    
    def buildTree( self, preorder: List[int], inorder: List[int] ) -> Optional[TreeNode]:
            
        if len( inorder ) < 1:
            return None
        
        o = inorder.index( preorder[0] )
        
        return TreeNode( inorder[o], self.buildTree( preorder[ 1 : o + 1 ], inorder[ : o ] ), self.buildTree( preorder[ o + 1 : ], inorder[ o + 1 : ] ) )
