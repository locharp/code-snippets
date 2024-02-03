class Solution:
    
    def numberOfPairs( self, points: List[ List[int] ] ) -> int:
        
        points.sort( key = lambda x: ( x[0], -x[1] ))
        n = len( points )
        ans = 0
        
        for i in range( n - 1 ):
            p, q = points[i]
            
            for j in range( i + 1, n ):
                r, s = points[j]
                
                if q < s:
                    continue
                    
                t = True
                
                for k in range( i + 1, j ):
                    u, v = points[k]
                    
                    if v <= q and v >= s:
                        t = False
                        break
                        
                if t:
                    ans += 1
                    
        return ans
