class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0
        d = collections.Counter( s )
        
        for m in d:
            for n in d:
                if m == n or d[m] < 2:
                    continue
                
                u = v = 0
                t = d[n]
                
                for ch in s:
                    if ch == m:
                        u += 1
                    elif ch == n:
                        v += 1
                        t -= 1
                        
                        if u - v < 0 and t > 0:
                            u = v = 0
                            
                    if v > 0:
                        ans = max( u - v, ans )
                        
        return ans