class Solution:
    def search( self, nums: List[int], target: int ) -> int:
        p, q = 0, len( nums ) - 1
        
        while p < q:
            i = ( p + q ) // 2
            
            if nums[i] < target:
                p = i + 1
            else:
                q = i
                
        return p if nums[p] == target else -1