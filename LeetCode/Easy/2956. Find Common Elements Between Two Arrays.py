class Solution:
    
    def findIntersectionValues( self, nums1: List[int], nums2: List[int] ) -> List[int]:
        
        c = Counter( nums1 )
        d = Counter( nums2 )
        
        return [ sum( c[i] for i in c if i in d ), sum( d[i] for i in d if i in c ) ]
