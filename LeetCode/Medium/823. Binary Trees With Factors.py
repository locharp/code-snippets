class Solution:

    def numFactoredBinaryTrees( self, arr: List[int] ) -> int:
        
        arr.sort()
        d = {}
        MOD = 1000000007
        
        for i in arr:
            c = 1

            for j in d:
                if i % j == 0 and i // j in d:
                    c = ( c + d[j] * d[ i // j ] ) % MOD

            d[i] = c

        return sum( d.values() ) % MOD
