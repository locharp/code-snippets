class Solution:
    def findRightInterval( self, intervals: List[List[int]] ) -> List[int]:
        d = sorted( ( j[0], i ) for i, j in enumerate( intervals ) )
        intervals = sorted( ( j[1], i ) for i, j in enumerate( intervals ) )
        n, j = len( d ), 0
        ans = [ -1 ] * n
        
        for i in range( n ):
            while j < n:
                if d[j][0] >= intervals[i][0]:
                    ans[ intervals[i][1] ] = d[j][1]
                    break
                else:
                    j += 1
                    
        return ans