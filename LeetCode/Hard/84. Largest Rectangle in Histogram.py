class Solution:
    def largestRectangleArea( self, heights: List[int] ) -> int:
        n = len( heights )
        q = []
        ans = 0
        
        for i in range( len( heights ) ):
            o = i
            
            while len( q ) > 0:
                if heights[i] < q[-1][0]:
                    r, o = q.pop()
                    ans = max( ( i - o ) * r, ans )
                else:
                    break
                    
            if len( q ) < 1 or q[-1][0] != heights[i]:
                q.append( ( heights[i], o ) )
            
        for i, j in q:
            ans = max( ( n - j ) * i, ans )
            
        return ans
