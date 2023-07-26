class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def on_time( s ):
            t = 0
            
            for d in dist:
                t = ceil( t ) + d / s
                
            return t <= hour
        
        p = 1
        q = 10000000
    b    ans = -1
        
        while p <= q:
            s = ( p + q ) // 2
            if on_time( s ):
                ans = s
                q = s - 1
            else:
                p = s + 1
                
        return ans