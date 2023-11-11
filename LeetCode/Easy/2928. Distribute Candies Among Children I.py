class Solution:
    
    def distributeCandies( self, n: int, limit: int ) -> int:
        
        ans = 0
        
        for i in range( max( n - limit * 2, 0 ), min( limit + 1, n + 1) ):
            for j in range( max( n - i - limit, 0 ), min( limit + 1, n - i + 1 ) ):
                ans += 1
                
        return ans
