class Solution:
    def champagneTower( self, poured: int, query_row: int, query_glass: int ) -> float:
        
        def f( m, n ):
            if d[m][n] < 0:
                d[m][n] = max( ( f( m - 1, n ) - 1 ) / 2, 0 )
            
                if n > 0:
                    d[m][n] += max( ( f( m - 1, n - 1 ) - 1 ) / 2, 0 )
                    
            return d[m][n]
        
        
        
        d = [ [ 0 ] * ( query_row + 1 ) for i in range( query_row + 1 ) ]
        d[0][0] = poured
        
        for i in range( 1, query_row + 1 ):
            for j in range( i + 1 ):
                d[i][j] = -1
                
        return min( f( query_row, query_glass ), 1 )
