class Solution:
    
    def maximumStrongPairXor( self, nums: List[int] ) -> int:
        
        a = []
        nums.sort()
        i = 0
        
        for j in range( 1, len( nums ) ):
            i = j - 1
            
            while i >= 0 and nums[j] - nums[i] <= nums[i]:
                a.append( nums[i] ^ nums[j] )
                i -= 1
                
        if len( a ) < 1:
            return 0
        
        return max( a )
