class Solution:

    def minSteps( self, s: str, t: str ) -> int:
        
        c = Counter( s )
        d = Counter( t )

        return sum( ( c - d ).values() )
