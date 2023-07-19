class Solution:
    def eraseOverlapIntervals( self, intervals: List[List[int]] ) -> int:
        p, ans = 0, 0
        intervals.sort( key = lambda x: x[1]  )
        
        for i in range( 1, len( intervals ) ):
            if intervals[p][1] > intervals[i][0]:
                ans += 1
            else:
                p = i
                
        return ans