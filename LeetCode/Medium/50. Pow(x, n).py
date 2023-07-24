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