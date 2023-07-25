class Solution:
    def peakIndexInMountainArray( self, arr: List[int] ) -> int:
        p = 1
        q = len( arr ) - 1
        ans = ( p + q ) // 2
        
        while p < q:
            if arr[ans] > arr[ ans + 1 ]:
                q = ans
            else:
                p = ans + 1
                
            ans = ( p + q ) // 2
            
        return ans