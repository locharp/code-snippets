class Solution:
    
    def findArray( self, pref: List[int] ) -> List[int]:

        k = pref[0]

        for i in range( 1, len( pref ) ):
            pref[i] ^= k
            k ^= pref[i]

        return pref
