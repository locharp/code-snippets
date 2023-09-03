class Solution:
    def uniquePaths( self, m: int, n: int ) -> int:
        if m == 1 or n == 1:
            return max( m, n )
        
        dp = [ [ 0 ] * n for _ in range( m ) ]
        
        for i in range( n ):
            dp[-1][i] = 1
            
        for i in range( m ):
            dp[i][-1] = 1
            
        for i in range( m - 2, -1, -1 ):
            for j in range( n - 2, -1, -1 ):
                dp[i][j] = dp[ i + 1 ][j] + dp[i][ j + 1 ]
                
        return dp[0][0]