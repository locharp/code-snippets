class Solution:
    def __init__( self ):
        self.d = {}
        
    def myPow( self, x: float, n: int ) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n in self.d:
            return self.d[n]
        elif n > 0:
            self.d[ n // 2 ] = self.myPow( x, n // 2 )
            self.d[ ( n + 1) // 2 ] = self.myPow( x, ( n + 1 ) // 2 )
            
            return self.d[ n // 2 ] * self.d[ ( n + 1 ) // 2 ]
        else:
            return 1 / self.myPow( x, -n )