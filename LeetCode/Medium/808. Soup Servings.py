class Solution:
    def soupServings( self, n: int ) -> float:
        n = ceil( n / 25 )
        o = { ( 4, 0 ), ( 3, 1 ), ( 2, 2 ), ( 1, 3 ) }
        dp = {}
        def f( x, y ):
            if ( x, y ) in dp:
                return dp[ ( x, y ) ]
                
            if x <= 0:
                if y <= 0:
                    return 0.5
                else:
                    return 1
            elif y <= 0:
                return 0
            
            q = 0
            for r, s in o:
                u = x - r
                v = y - s
                
                dp[ ( u, v ) ] = f( u, v )
                q += 0.25 * dp[ ( u, v ) ]
                
            return q
        
        for i in range( n ):
            for j in range( i ):
                if f( i, j ) > 1 - 1e-5:
                    return 1
                
        return f( n, n )