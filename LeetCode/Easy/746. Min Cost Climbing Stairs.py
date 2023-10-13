class Solution:
    
    def __init__( self ):
        
        self.d = [ -1 ] * 1000
        
        
        
    def f( self, cost, i):
        
        if i >= len( cost ):
            return 0
        elif self.d[i] != -1:
            return self.d[i]
            
        self.d[i] = cost[i] + min( self.f( cost, i + 1 ), self.f( cost, i + 2 ) )
        
        return self.d[i]
    
        
        
    def minCostClimbingStairs( self, cost: List[int], i = 0 ) -> int:
        
        return min( self.f( cost, 0 ), self.f( cost, 1 ) )
