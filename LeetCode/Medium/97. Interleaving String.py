class Solution:
    def isInterleave( self, s1: str, s2: str, s3: str ) -> bool:
        m, n = len( s1 ), len( s2 )
        o = len( s3 )
        
        if m + n != o:
            return False
        
        if m == 0:
            return s2 == s3
        elif n == 0:
            return s1 == s3
            
        dp = [ True ] * ( n + 1 )
        
        for i in range(n ):
            dp[ i + 1 ] = dp[i] and s2[i] == s3[i]
        
        for i in range( m ):
            dp[0] = dp[0] and s1[i] == s3[i]
            
            for j in range( n ):
                dp[ j + 1 ] = dp[j] and s2[ j ] == s3[ i + j + 1 ] or dp[ j + 1 ] and s1[i] == s3[ i + j + 1 ]
                
        return dp[-1]