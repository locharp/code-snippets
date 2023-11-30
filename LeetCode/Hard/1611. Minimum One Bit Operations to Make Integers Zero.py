class Solution:
    
    def __init__( self ):
        
        self.a = []
        
        
        
    def f( self, s, i, o ):
        
        if i == len( s ):
            return 0
        
        if s[i] == "1":
            return self.a[i] * o + self.f( s, i + 1, -o )
        else:
            return self.f( s, i + 1, o )
        
        
        
    def minimumOneBitOperations( self, n: int ) -> int:
        
        s = bin( n )[ 2 : ]
        self.a = [ 2 ** i - 1 for i in range( len( s ), 0, -1 ) ]
        
        return self.f( s, 0, 1 )
