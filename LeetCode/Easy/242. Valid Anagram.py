from collections import Counter as count

class Solution:
    def isAnagram( self, s: str, t: str ) -> bool:
        return count( s ) == count( t )