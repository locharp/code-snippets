from collections import defaultdict

class Solution:

    def sortByBits( self, arr: List[int] ) -> List[int]:

        d = defaultdict( list )

        for i in arr:
            d[ i.bit_count() ].append( i )

        return [ j for i in sorted( d ) for j in sorted( d[i] ) ]
