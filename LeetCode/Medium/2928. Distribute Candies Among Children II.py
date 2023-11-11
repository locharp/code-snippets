class Solution:
    
    def distributeCandies( self, n: int, limit: int ) -> int:
        
        ans = 0
        
        for i in range( max( n - 2 * limit, 0 ), min( n, limit ) + 1 ):
            ans += 1 + min( n - i, limit ) - max( n - i - limit, 0 )
            
        return ans
