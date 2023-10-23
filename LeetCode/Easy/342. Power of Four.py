class Solution:

    def isPowerOfFour( self, n: int ) -> bool:
        
        return log( n, 4 ).is_integer()
