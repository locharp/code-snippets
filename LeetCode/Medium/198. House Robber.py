class Solution:
    def rob( self, nums: List[int], p: int = 0, q : int = 0) -> int:
        if len( nums ) == 0:
            return max( p, q )
        
        return self.rob( nums[ 1 : ], q, max( nums[0] + p, q ) ) 