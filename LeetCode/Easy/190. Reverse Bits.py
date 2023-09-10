class Solution:
    def reverseBits( self, n: int ) -> int:
        return int( bin( n )[ : 1 : -1 ].ljust( 32, "0" ), 2 )