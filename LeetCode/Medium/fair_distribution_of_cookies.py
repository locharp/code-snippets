class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len( cookies )
        
        if n == k:
            return max( cookies )
        
        curr = [ 0 ] * k
        def dfs( i ):
            if i == n:
                return max( curr )
            
            ans = float( "inf" )
            for j in range( k ):
                curr[j] += cookies[i]
                
                ans = min( ans, dfs( i + 1 ) )
                
                curr[j] -= cookies[i]
                
            return ans
        
        return dfs( 0 )