class Solution:
    def constructProductMatrix( self, grid: List[ List[int] ] ) -> List[ List[int] ]:
        n, m = len( grid ), len( grid[0] )
        o = [ j for i in grid for j in i ]
        p = [ 1, 1 ] + o
        q = 1
        
        for i in range( 2, len( p ) - 1 ):
            p[i] = p[i] * p[ i - 1 ] % 12345
        
        for i in range( len( o ) - 1, 0, -1 ):
            q *= o[i]
            p[i] = p[i] * q % 12345
        
        p = p[ 1 : -1 ]
        
        for i in range( n ):
            for j in range( m ):
                grid[i][j] = p[ i * m + j ]
                
        return grid
