class Solution:
    
    def getSumAbsoluteDifferences( self, nums: List[int] ) -> List[int]:
        
        n = len( nums )
        total = sum( nums )
        pre = 0
        result = []
        
        for i in range( len( nums ) ):
            p = i * nums[i] - pre
            q = total - pre - ( n - i ) * nums[i]
            result.append( p + q )
            pre += nums[i]
            
        return result
