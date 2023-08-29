class Solution:
    def bestClosingTime( self, customers: str ) -> int:
        ans = -1
        m = n = 0
        
        for i, j in enumerate( customers ):
            if j == "Y":
                n -= 1
                
                if n < m:
                    m = n
                    ans = i
            else:
                n += 1
                
        return ans + 1