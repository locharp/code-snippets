class Solution:

    def countPalindromicSubsequence( self, s: str ) -> int:
        
        d = defaultdict( list )

        for i, j in enumerate( s ):
            d[j].append( i )
        
        return sum( len( set( s[ j[0] + 1 : j[-1] ] ) ) for i, j in d.items() if len( j ) > 1 )
