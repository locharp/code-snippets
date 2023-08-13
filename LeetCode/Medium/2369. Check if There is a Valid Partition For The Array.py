class Solution:
    def validPartition( self, nums: List[int] ) -> bool:
        q = len( nums )
        o = q - 2
        dp = [ 0 ]
        
        while dp:
            i = dp.pop()
            
            if i < o:
                if nums[i] == nums[ i + 1 ]:
                    i += 2
                
                    if nums[i] == nums[ i - 1 ]:
                        while i < q and nums[i] == nums[ i - 1 ]:
                            i += 1
                        
                        dp = [ i, i - 1 ]
                    else:
                        dp += [ i ]
                    
                elif nums[i] + 1 == nums[ i + 1 ]:
                    j = i + 2
                    
                    while j < q and nums[j] - 1 == nums[ j - 1 ]:
                        j += 1
                        
                    j -= i
                    
                    if j >= 3:
                        dp += [ i + j // 3 * 3 ]
            elif i == o and nums[i] == nums[ i + 1 ] or i == q:
                return True
            
        return False