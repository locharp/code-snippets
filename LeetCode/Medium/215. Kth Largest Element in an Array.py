class Solution:
    def findKthLargest( self, nums: List[int], k: int ) -> int:
        m = 0
        n = len( nums ) - 1
        k = n - k + 1
        
        while True:
            p = nums[k]
            nums[n], nums[k] = nums[k], nums[n]
            i = m
            
            for j in range( m, n + 1 ):
                if nums[j] < p:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    
            nums[i], nums[n] = p, nums[i]
            
            if i == k:
                return nums[i]
            elif i < k:
                m = i + 1
            else:
                n = i - 1