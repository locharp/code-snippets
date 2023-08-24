class Solution:
    def fullJustify( self, words: List[str], maxWidth: int ) -> List[str]:
        ans = [ [] ]
        n = -1
        
        for word in words:
            m = len( word ) + 1
            
            if n + m > maxWidth:
                q = len( ans[-1] ) - 1
                r = maxWidth - sum( len( j ) for j in ans[-1] )            
                if q == 0:
                    ans[-1] = ans[-1][0] + " " * r
                else:
                    o = r // q
                    p = r % q
                    
                    for j in range( p ):
                        ans[-1][j] += " "
                        
                    ans[-1] = ( " " * o ).join( ans[-1] )
                ans.append( [ word ] )
                n = m - 1
            else:
                ans[-1].append( word )
                n += m
                
        ans[-1] = " ".join( ans[-1] )
        ans[-1] += " " * ( maxWidth - len( ans[-1] ) )
        
        return ans