class Solution:
    def majorityElement( self, nums: List[int] ) -> List[int]:
        c = Counter( nums )
        
        return [ i for i, j in c.items() if j > len( nums ) // 3 ]
