class Solution:
    
    def __init__( self ):
        
        self.a = [ [ 4, 6 ], [ 6, 8 ], [ 7, 9 ], [ 4, 8 ], [ 3, 9, 0 ], [], [ 1, 7, 0 ], [ 2, 6 ], [ 1, 3 ], [ 2, 4 ] ]
        self.MOD = 10 ** 9 + 7
        
        
    def f( self, a, n ):
    
        if n < 2:
            return a
            
        res = [ 0 ] * 10
        
        for i in range( 10 ):
            for j in self.a[i]:
                res[j] = ( res[j] + a[i] ) % self.MOD
                
        return self.f( res, n - 1 )
        
        
        
    def knightDialer( self, n: int ) -> int:
        
        return sum( self.f( [ 1 ] * 10, n ) ) % self.MOD
