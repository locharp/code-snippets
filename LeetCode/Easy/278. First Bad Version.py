class Solution:
    def firstBadVersion( self, n: int ) -> int:
        m = 0
        
        while m < n:
            o = ( m + n ) // 2
            
            if isBadVersion( o ):
                n = o
            else:
                m = o + 1
                
        return n