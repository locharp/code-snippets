class Solution:
    def countPrimes( self, n: int ) -> int:
        a = [ 1 ] * n 
        
        for i in range( 2, floor( pow( n, .5 ) ) + 1 ):
            if a[ i ] == 0:
                continue
                
            for j in range( i * 2, n, i ):
                a[j] = 0
                z
        return sum( a[ 2 : ] )