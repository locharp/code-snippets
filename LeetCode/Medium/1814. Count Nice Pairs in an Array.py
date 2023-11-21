class Solution:
    
    def countNicePairs( self, nums: List[int] ) -> int:
        
        d = defaultdict( int )
        ans = 0
        MOD = 10 ** 9 + 7
        
        for num in nums:
            n = num - int( str( num )[ : : -1 ] )
            ans = ( ans + d[n] ) % MOD
            d[n] += 1
            
        return ans
