class Solution:
    def isMonotonic( self, nums: List[int] ) -> bool:
        n = len( nums )
        i = 1
        
        while i < n and nums[i] == nums[ i - 1 ]:
            i += 1
            
        if i == n:
            return True
        
        if nums[i] >= nums[ i - 1 ]:
            for j in range( i + 1, n ):
                if nums[j] < nums[ j - 1 ]:
                    return False
        else:
            for j in range( i + 1, n ):
                if nums[j] > nums[ j - 1 ]:
                    return False
                
        return True
