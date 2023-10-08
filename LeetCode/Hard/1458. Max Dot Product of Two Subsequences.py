class Solution:
    def maxDotProduct( self, nums1: List[int], nums2: List[int] ) -> int:
        
        m, n = len( nums1 ), len( nums2 )
        dp = [ -1000001 ] * ( n + 1 )
        dp2 = [ -1000001 ] * ( n + 1 )
        
        for i in range( n -1, -1, -1 ):
            dp2[i] = max( nums2[i] * nums1[-1], dp2[ i + 1 ] )
            
        for i in range( m - 2, -1, -1 ):
            for j in range( n - 1, -1, -1):
                o = nums1[i] * nums2[j]
                dp[j] = max( o, o + dp2[ j + 1 ], dp[ j + 1 ], dp2[j] )
            
            dp2 = dp
            dp = [ -1000001 ] * ( n + 1 )
            
        return max( dp2 )
