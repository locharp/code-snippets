class Solution:
    
    def getGoodIndices( self, variables: List[ List[int] ], target: int ) -> List[int]:
        
        return [ i for i, j in enumerate( variables ) if ( ( ( j[0] ** j[1] ) % 10 ) ** j[2] ) % j[3] == target ]
        
