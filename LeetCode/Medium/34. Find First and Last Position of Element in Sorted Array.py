class Solution:
    def searchRange( self, nums: List[int], target: int ) -> List[int]:
        n = len( nums )
        
        if n == 0:
            return [ -1, -1 ]
        
        i = j = bisect_left( nums, target )
        
        if i == n or nums[i] != target:
            return [ -1, -1 ]
        
        while j < len( nums ) and nums[j] == target:
            j += 1
            
        return  [ i, j - 1 ]