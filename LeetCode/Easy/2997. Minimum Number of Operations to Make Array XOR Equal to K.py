class Solution:
    
    def minOperations( self, nums: List[int], k: int ) -> int:
        
        for i in nums:
            k ^= i
            
        return k.bit_count()
