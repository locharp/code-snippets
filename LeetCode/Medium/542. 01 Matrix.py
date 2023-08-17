class Solution:
    def updateMatrix( self, mat: List[List[int]] ) -> List[List[int]]:
        m, n = len( mat ), len( mat[0] )
        p, q = m - 1, n - 1
        ans = [ [ 1000000 ] * n for _ in range( m ) ]
        ans[0][0] = mat[0][0] * 1000000
        
        for i in range( 1, m ):
            ans[i][0] = min( mat[i][0] * 1000000, ans[ i - 1 ][0] + 1)
            
        for i in range( 1, n ):
            ans[0][i] = min( mat[0][i] * 1000000, ans[0][ i - 1 ] + 1 )
            
        for i in range( 1, m ):
            for j in range( 1, n ):
                ans[i][j] = min( mat[i][j] * 1000000, ans[ i - 1 ][j] + 1, ans[i][ j - 1 ] + 1 )
                
        for i in range( m - 2, -1, -1 ):
            ans[i][q] = min( ans[i][q], ans[ i + 1 ][q] + 1 )
            
        for i in range( n - 2, -1 , -1 ):
            ans[p][i] = min( ans[p][i], ans[p][ i + 1 ] + 1 )
            
        for i in range( m - 2, -1, -1 ):
            for j in range( n - 2, -1, -1 ):
                ans[i][j] = min( ans[i][j], ans[ i + 1 ][j] + 1, ans[i][ j + 1 ] + 1 )
                
        return ans