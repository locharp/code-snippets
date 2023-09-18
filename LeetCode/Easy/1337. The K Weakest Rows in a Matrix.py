class Solution:
    def kWeakestRows( self, mat: List[ List[int] ], k: int ) -> List[int]:
        d = defaultdict( list )
        
        for i in range( len( mat ) ):
            d[ sum( mat[i] ) ].append( i )
            
        ans = []
        
        for i, j in sorted( d.items() ):
            ans += j
            
        return ans[ : k ]