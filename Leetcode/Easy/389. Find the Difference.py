class Solution:
    def findTheDifference( self, s: str, t: str ) -> str:
        s = Counter( s )
        t = Counter( t )
        
        for ch in t:
            if ch not in s or t[ch] > s[ch]:
                return ch
