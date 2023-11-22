class Solution:
    
    def findDiagonalOrder( self, nums: List[ List[int] ] ) -> List[int]:
        
        d = defaultdict( list )
        ans = []
        
        for i in range( len( nums ) - 1, -1, -1 ):
            for j in range( len( nums[i] ) ):
                d[ i + j ].append( nums[i][j] )
                
        for i in sorted( d ):
            ans += d[i]
            
        return ans
