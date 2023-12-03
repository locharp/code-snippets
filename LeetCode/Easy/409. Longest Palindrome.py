class Solution:

    def longestPalindrome( self, s: str ) -> int:
        
        c = Counter( s )
        ans = 0
        o = False

        for i in c.values():
            if i % 2 > 0:
                o = True
                ans += i - 1
            else:
                ans += i

        if o:
            return ans + 1
        else:
            return ans
