class Solution:
    def minimumAbsDifference( self, arr: List[int] ) -> List[List[int]]:
        arr.sort()
        d = defaultdict( list )
        
        for i in range( len( arr ) - 1 ):
            d[ arr[ i + 1 ] - arr[i] ].append( [ arr[i], arr[ i + 1 ] ] )
            
        return d[ sorted( d )[0] ]