class Solution:
    def myPow( self, x: float, n: int ) -> float:
        if n < 0:
            x = 1 / x
            n = -n
            
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= x
                n -= 1
                
            x *= x
            n //= 2
            
        return ans



# 2
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
