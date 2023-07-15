class Solution:
    def maxValue( self, events: List[List[int]], k: int ) -> int:
        events.sort()
        starts = [ s for s, _, _ in events ]
        m = len( events )
        d = {}
        
        def dfs( i, j ):
            s, e, v = events[i]
            if j == 1:
                return v
            
            n = bisect_right( starts, e )
            
            if ( i, j ) in d:
                return d[( i, j )]
            
            d[( i, j )] = v
            for o in range( n, m ):
                d[( i, j )] = max( d[( i, j )], v + dfs( o, j - 1 ) )
                
            return d[( i, j )]
        
        return max( [ dfs( i, k ) for i in range( m ) ])