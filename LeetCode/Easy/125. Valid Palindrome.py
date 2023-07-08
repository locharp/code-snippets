class Solution:
    def isPalindrome( self, s: str ) -> bool:
        t = [ c for c in s.lower() if c.isalnum() ]
        m = len( t ) // 2
        
        return t[ : m ] == t[ -1 : -m - 1 : -1 ]