class Solution:
    def knightProbability( self, n: int, k: int, row: int, column: int ) -> float:
        if k == 0:
            return 1
        
        ds = ( ( -2, -1 ), ( -2, 1 ), ( 2, -1 ), ( 2, 1 ), ( -1, 2 ), ( 1, 2 ), ( -1, -2 ), ( 1, -2 ) )
        dp = {}
        
        def dfs( r, c, k, ds):
            if ( r, c, k ) in dp:
                return dp[ ( r, c, k ) ]
            
            p = 0
            
            for u, v in ds:
                u += r
                v += c
                
                if 0 <= u < n and 0 <= v < n:
                    if k > 1:
                        p += dfs( u, v, k - 1, ds )
                    else:
                        p += 1
                        
            dp[ ( r, c, k ) ] = p
                    
            return p
        
        p = dfs( row, column, k, ds)
        
        return p / 8 ** k