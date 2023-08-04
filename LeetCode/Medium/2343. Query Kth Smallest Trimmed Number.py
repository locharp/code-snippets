class Solution:
    def smallestTrimmedNumbers( self, nums: List[str], queries: List[List[int]] ) -> List[int]:
        n = len( nums[0] )
        d = {}
        ans = []
        
        for k, t in queries:
            if t not in d:
                d[t] = sorted( map( lambda num: ( num[1][ n - t : ], num[0] ), enumerate( nums ) ) )
                
            ans.append( d[t][ k - 1 ][1] )
            
        return ans