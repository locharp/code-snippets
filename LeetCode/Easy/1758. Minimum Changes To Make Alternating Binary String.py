class Solution:

    def f( self, s, i, k ):
        
        if i == len( s ):
            return k

        if i % 2 > 0:
            if s[i] == "1":
                k += 1
        elif s[i] == "0":
            k += 1

        return self.f( s, i + 1, k)



    def minOperations( self, s: str ) -> int:
        
        k = self.f( s, 0, 0 )

        return min( k, len( s ) - k )
