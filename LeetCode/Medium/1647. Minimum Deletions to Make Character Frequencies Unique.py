class Solution:
    def minDeletions( self, s: str ) -> int:
        s = Counter( s ).values()
        t = Counter( s )
        r = [ False if i in s else True for i in range( max( t ) ) ]
        ans = 0
        
        for i, j in t.items():
            for k in range( 1, j ):
                u = i - 1
                
                while u > 0:
                    if r[u]:
                        r[u] = False
                        ans += i - u
                        break
                        
                    u -= 1
                    
                if u == 0:
                    ans += i
                    
        return ans