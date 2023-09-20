class Solution:
    def minOperations( self, nums: List[int], x: int ) -> int:
        i = y = 0
        m = n = len( nums )
        o = 100001
        
        while i < n:
            y += nums[i]
            i += 1
            if y >= x:
                break
                
        if y == x:
            o = i
        elif i >= n:
            return -1
        
        while i > 0:
            i -= 1
            y -= nums[i]
            
            while y < x:
                m -= 1
                y += nums[m]
                
            if y == x:
                o = min( i + n - m, o )
                
        return o if o < 100001 else -1