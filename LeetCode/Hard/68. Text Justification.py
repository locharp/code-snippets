class Solution:
    def fullJustify( self, words: List[str], maxWidth: int ) -> List[str]:
        ans = [ [] ]
        n = -1
        
        for word in words:
            m = len( word ) + 1
            
            if n + m > maxWidth:
                ans.append( [ word ] )
                n = m - 1
            else:
                ans[-1].append( word )
                n += m
            
        for i in range( len( ans ) - 1 ):
            m = len( ans[i] ) - 1
            
            if m == 0:
                ans[i] = ans[i][0] + " " * ( maxWidth - len( ans[i][0] ) )
                continue
                
            n = maxWidth - sum( len( j ) for j in ans[i] )
            o = n // m
            p = n % m
            
            for j in range( p ):
                ans[i][j] += " "
                
            ans[i] = ( " " * o ).join( ans[i] )
        
        ans[-1] = " ".join( ans[-1] )
        ans[-1] += " " * ( maxWidth - len( ans[-1] ) )
        
        return ans
