class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len( nums )
        sum = 0
        count = n + 1
        j = 0
        
        for i in range( n ):
            while j < n and sum < target:
                sum += nums[j]
                j += 1
            
            if sum >= target:
                count = min( j - i, count )

            sum -= nums[i]
            
        return count if count <= n else 0