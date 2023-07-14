class Solution:
    def longestSubsequence( self, arr: List[int], difference: int ) -> int:
        d = {}
        
        for i in arr:
            d[i] = d.get( i - difference, 0 ) + 1
            
        return max( d.values() )