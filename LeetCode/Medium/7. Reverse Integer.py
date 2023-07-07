class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            n = -int( str( abs(x) )[::-1] )
        else:
            n = int( str( x )[::-1] )
            
        return 0 if n > 2 ** 31 - 1 or n < -( 2 ** 31 ) else n