class Solution:
    def isReachableAtTime( self, sx: int, sy: int, fx: int, fy: int, t: int ) -> bool:
        
        x = abs( fx - sx )
        y = abs( fy - sy )
        m = max( x, y )
        
        if t == 1 and m < 1:
            return False
        
        return t >= m
