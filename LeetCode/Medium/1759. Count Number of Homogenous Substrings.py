@cache
def f( n ):
    if n < 2:
        return n
        
    return n + f( n - 1 )
    




class Solution:

    def countHomogenous( self, s: str ) -> int:
        
        d = defaultdict( int )
        t = s[0]
        c = 1
        MOD = 10 ** 9 + 7
        ans = 0

        for i in range( 1, len( s ) ):
            if s[i] == t:
                c += 1
            else:
                d[ t * c ] += 1
                t = s[i]
                c = 1

        d[ t * c ] += 1

        for i, j in d.items():
            ans = ( ans + f( len( i ) ) * j ) % MOD
        
        return ans
