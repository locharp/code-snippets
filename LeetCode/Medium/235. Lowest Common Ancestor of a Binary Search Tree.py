class Solution:
    def lowestCommonAncestor( self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode' ) -> 'TreeNode':
        m = [ root ]
        n = [ root ]
        
        def f( r, s, a ):
            while r != s:
                if r.val > s.val:
                    r = r.left;
                else:
                    r = r.right
                
                a.append( r )
                
        f( root, p, m )
        f( root, q, n )
        o = min( len( m ), len( n ) )
        
        for i in range( o ):
            if m[i] != n[i]:
                return m[ i - 1 ]
                
        return m[ o - 1 ]