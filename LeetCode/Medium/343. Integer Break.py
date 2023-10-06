class Solution:
    def integerBreak( self, n: int ) -> int:
        if n < 8:
            return n // 2 * ( ( n + 1 ) // 2 )
        
        p, q = divmod( n, 3 )
        
        if q == 1:
            p -= 1
            q = 4
            
        return 3 ** p * max( q, 1 )
