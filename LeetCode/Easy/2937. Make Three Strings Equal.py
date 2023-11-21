class Solution:
    
    def findMinimumOperations( self, s1: str, s2: str, s3: str ) -> int:
        
        i = 0
        m = min( len( s1 ), len( s2 ), len( s3 ) )
        
        while i < m and s1[i] == s2[i] and s2[i] == s3[i]:
            i += 1
            
        if i < 1:
            return -1
        else:
            return sum( [ len( s1 ), len( s2 ), len( s3 ) ] ) - 3 * i
