class Solution:
    def findLongestChain( self, pairs: List[List[int]] ) -> int:
        ans, p = 0, -1001
        
        for m, n in sorted( pairs, key = lambda o: o[1] ):
            if m > p:
                p = n
                ans += 1
                
        return ans