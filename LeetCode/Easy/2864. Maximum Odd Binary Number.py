class Solution:
    def maximumOddBinaryNumber( self, s: str ) -> str:
        n = len( s )
        z = s.count( "1" )
        
        return "1" * ( z - 1 ) + "0" * ( n - z ) + "1"