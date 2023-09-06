class Solution:
    dp = [ 1, 1 ]
    
    def climbStairs( self, n: int ) -> int:
        if n >= len( self.dp ):
            self.dp.append( self.climbStairs( n - 1 ) + self.climbStairs( n - 2 ) )
        
        return self.dp[n]