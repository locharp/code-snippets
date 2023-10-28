class Solution:

    def countVowelPermutation( self, n: int ) -> int:
        
        d = [ 1 ] * 5
        MOD = 10 ** 9 + 7
        
        for i in range( 1, n ):
            c = [ j for j in d ]
            d[0] = c[1] + c[2] + c[4] % MOD
            d[1] = c[0] + c[2] % MOD
            d[2] = c[1] + c[3] % MOD
            d[3] = c[2] % MOD
            d[4] = c[2] + c[3] % MOD

        return sum( d ) % MOD
