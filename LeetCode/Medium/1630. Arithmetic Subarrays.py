class Solution:
    
    def checkArithmeticSubarrays( self, nums: List[int], l: List[int], r: List[int] ) -> List[bool]:
        
        ans = []
        
        for i in range( len( r ) ):
            a = sorted( nums[ l[i] : r[i] + 1 ] )
            o = a[1] - a[0]
            t = True
            
            for j in range( 2, len( a ) ):
                if a[j] - a[ j - 1 ] != o:
                    t = False
                    break
                    
            ans.append( t )
            
        return ans
