class Solution:
    def longestSubarray( self, nums: List[int] ) -> int:
        n = len( nums )
        start = -1
        last = -1
        i = 0
        
        while i < n and ( start == -1 or last == -1 ):
            if start < 0 and nums[i] == 1:
                start = i
                
            if last < 0 and nums[i] != 1:
                last = i
                
            i += 1
                
        if start < 0:
            return 0
        
        if last < 0:
            return n - 1
        
        count = last - start
        
        if count < 1:
            count = i - 1
        
        ans = count
        while i < n:
            if nums[i] != 1:
                count = i - start - 1
                ans = max( count, ans )
                start = last + 1
                last = i
            i += 1
        
        if nums[last] != n - 1:
            count = i - start - 1
            ans = max( count, ans )
            
        return ans