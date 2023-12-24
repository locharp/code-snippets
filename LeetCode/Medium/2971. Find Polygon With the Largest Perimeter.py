class Solution:
    
    def largestPerimeter( self, nums: List[int] ) -> int:
        
        nums.sort()
        ans = -1
        curr = nums[0] + nums[1]
        
        for i in nums[ 2 : ]:
            curr += i
            
            if curr - i > i:
                ans = curr
            
        return ans
