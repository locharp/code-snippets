class Solution:
    
    @cache
    def f( self, nums, k, i ):
        
        if i == len( nums ):
            return 1 if k == 0 else 0
        
        return self.f( nums, k + nums[i], i + 1 ) + self.f( nums, k - nums[i], i + 1 )
    
    
    
    def findTargetSumWays( self, nums: List[int], target: int ) -> int:
        
        return self.f( tuple( nums ), target, 0 )
