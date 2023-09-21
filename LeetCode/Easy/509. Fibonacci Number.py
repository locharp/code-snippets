class Solution:
    def __init__( self ):
        self.d = [ 0 ] * 31
        self.d[1] = 1
        
    def fib( self, n: int ) -> int:
        if n < 2 or self.d[n] != 0:
            return self.d[n]
        
        return self.fib( n - 2 ) + self.fib( n - 1 )