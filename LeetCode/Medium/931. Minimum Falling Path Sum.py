class Solution:

    def minFallingPathSum( self, matrix: List[ List[int] ] ) -> int:
        
        n = len( matrix )
        m = len( matrix[0] )
        
        for i in range( 1, n ):
            h = i - 1

            for j in range( m ):
                matrix[i][j] += min( matrix[h][ max( j - 1, 0 ) : min( j + 2, m ) ] )

        return min( matrix[ m - 1 ] )
