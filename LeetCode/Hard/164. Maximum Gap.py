class Solution:
    def maximumGap( self, nums: List[int] ) -> int:
        def sort( a, p ):
            if p < 1 or len( a ) < 2:
                return
            
            gs = [ [] for _ in range( 10 ) ]
            
            for x in a:
                gs[ x // p % 10 ].append( x )
            
            p //= 10 
            
            for g in gs:
                sort( g, p )
                
            a[ : ] = [ i for g in gs for i in g ]
            
        ans = 0
        sort( nums, 10 ** ( len( str( max( nums ) ) ) - 1 ) )
        
        for i in range( len( nums ) - 2, -1, -1 ):
            ans = max( ans, nums[ i + 1 ] - nums[ i ] )
                
            if ans >= nums[i]:
                break
            
        return ans