# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def f( self, root, a, o ):
        
        if root is None:
            return False
        
        a.append( root )
        
        if root == o:
            return True
        
        if self.f( root.left, a, o ) or self.f( root.right, a, o ):
            return True
        else:
            a.pop()
            
            return False
        
        
            
    def lowestCommonAncestor( self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode' ) -> 'TreeNode':
        
        m = []
        n = []
        
        self.f( root, m, p )
        self.f( root, n, q )
        
        o = min( len( m ), len( n ) )
        
        for i in range( 1, o + 1 ):
            if i == o or m[i] != n[i]:
                return m[ i - 1 ]
