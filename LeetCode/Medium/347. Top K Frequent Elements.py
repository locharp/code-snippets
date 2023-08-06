class Solution:
    def topKFrequent( self, nums: List[int], k: int ) -> List[int]:
        nums = Counter( nums )
        
        return sorted( nums, key = lambda i: nums[i], reverse = True )[ : k ]