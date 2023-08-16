class Solution:
    def __init__( self, nums: List[int] ):
        self.nums = nums  
        
    def reset( self ) -> List[int]:
        return self.nums
        
    def shuffle( self ) -> List[int]:
        return sample( self.nums, len( self.nums ) )