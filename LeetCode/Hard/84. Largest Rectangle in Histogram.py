class Solution:
    def largestRectangleArea( self, heights: List[int] ) -> int:
        n = len( heights )
        q = []
        ans = 0
        
        for i in range( len( heights ) ):
            o = i
            
            while len( q ) > 0:
                r, s = heappop( q )
                
                if heights[i] == -r:
                    o = s
                    break
                elif heights[i] < -r:
                    o = min( o, s )
                    ans = max( ( i - s ) * -r, ans )
                else:
                    heappush( q, ( r, s ) )
                    break
                        
            heappush( q, ( -heights[i], o ) )
            
        for i, j in q:
            ans = max( ( n - j ) * -i, ans )
            
        return ans
