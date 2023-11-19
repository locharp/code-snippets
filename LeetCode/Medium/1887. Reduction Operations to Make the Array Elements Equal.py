class Solution:
    
    def reductionOperations( self, nums: List[int] ) -> int:
        
        nums.sort()
        ans = x = 0
        
        for i in range( 1, len( nums ) ):
            if nums[i] > nums[ i - 1 ]:
                x += 1
                
            ans += x
            
        return ans
