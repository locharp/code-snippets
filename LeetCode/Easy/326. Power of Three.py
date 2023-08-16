class Solution:
    def isPowerOfThree( self, n: int ) -> bool:
        return False if n < 1 else abs( round( log( n, 3 ) ) - log( n, 3 ) ) < 0.0000000001