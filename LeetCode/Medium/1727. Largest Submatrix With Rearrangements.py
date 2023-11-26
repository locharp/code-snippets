class Solution:
    
    def largestSubmatrix( self, matrix: List[ List[int] ] ) -> int:
        
        m = len( matrix[0] )
        ans = matrix[0].count( 1 )
        
        for i in range( 1, len( matrix ) ):
            a = []
            
            for j in range( m ):
                if matrix[i][j] > 0:
                    matrix[i][j] += matrix[ i - 1 ][j]
                    a.append( matrix[i][j] )
                    
            a.sort( reverse = True )
            
            if len( a ) > 0:
                ans = max( ans, max( ( i + 1 ) * a[i] for i in range( len( a ) ) ) )
            
        return ans
