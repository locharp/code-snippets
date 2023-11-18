class Solution:
    
    def maxFrequency( self, nums: List[int], k: int ) -> int:
        
        nums.sort()
        i = g = 0
        
        for j in range( len( nums ) ):
            g += nums[j]
            
            if ( j - i + 1 ) * nums[j] - g > k:
                g -= nums[i]
                i += 1
                
        return j - i + 1
