from collections import defaultdict

class Solution:
    
    def f( self, r, e, v, u ):
        
        m = v[r]
        n = 0
        
        for i in e[r]:
            if i in u:
                continue
                
            p, q = self.f( i, e, v, u | { i } )
            m += p
            n += q

        n = v[r] if n < 1 else min( n, v[r] )
        
        return ( m, n )
    
    
    
    def maximumScoreAfterOperations( self, edges: List[ List[int] ], values: List[int] ) -> int:
        
        e = defaultdict( list )
        
        for i, j in edges:
            e[i].append( j )
            
        i, j = self.f( 0, e, values, { 0 } )
        
        return i - j
