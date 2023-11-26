class Solution:
    
    def minimumCoins( self, prices: List[int] ) -> int:
        
        n = len( prices )
        
        @cache
        def f( i, j = 3 ):
            if i >= n:
                return 0
            
            m = inf
            
            for k in range( i + 1, j ):
                m = min( m, f( k, ( k + 1 ) * 2 + 1 ) )
                
            return prices[i] + m
        
        return f( 0 )
