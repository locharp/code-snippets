class Solution:
    def findDisappearedNumbers( self, nums: List[int] ) -> List[int]:
        s = set( range( 1, len ( nums ) + 1 ) )
        
        return list( s.difference( set( nums ) ) )