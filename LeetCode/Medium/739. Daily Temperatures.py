class Solution:
    
    def dailyTemperatures( self, temperatures: List[int] ) -> List[int]:
        
        ans = [ 0 ] * len( temperatures )
        a = [ 0 ]
        
        for i in range( 1, len( temperatures ) ):
            while len( a ) > 0 and temperatures[ a[-1] ] < temperatures[i]:
                k = a.pop()
                ans[k] = i - k
            
            a.append( i )
                    
        return ans
