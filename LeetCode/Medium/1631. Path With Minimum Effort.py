class Solution:
    def minimumEffortPath( self, heights: List[ List[int] ] ) -> int:
        m = len( heights ) - 1
        n = len( heights[0] ) - 1
        c = [ [ True ] * ( n + 1 ) for i in range( m + 1 ) ]
        d = ( ( 0, 1 ), ( 1, 0 ), ( 0, -1 ), ( -1, 0 ) )
        o = 0
        q = []
        heappush( q, ( 0, 0, 0 ) )
        
        while True:
            p, r, s = heappop( q )
            c[r][s] = False
            o = max( o, p )
            
            if r == m and s == n:
                return o
                
            for e, f in d:
                g = e + r
                h = f + s
                
                if g >= 0 and g <= m and h >= 0 and h <= n and c[g][h]:
                    heappush( q, ( abs( heights[r][s] - heights[g][h] ), g, h ) )