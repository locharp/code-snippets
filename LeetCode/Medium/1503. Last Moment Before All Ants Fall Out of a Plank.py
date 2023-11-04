class Solution:
    
    def getLastMoment( self, n: int, left: List[int], right: List[int] ) -> int:
        
        p = max( left ) if len( left ) > 0 else 0
        q = min( right ) if len( right ) > 0 else n
        
        return max( p, n - q )
