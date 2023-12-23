class Solution:

    def maxWidthOfVerticalArea( self, points: List[ List[int] ] ) -> int:
        
        a = sorted( { i for i, j in points } )
        
        if len( a ) < 2:
            return 0
        
        return max( a[i] - a[ i - 1 ] for i in range( 1, len( a ) ) )
