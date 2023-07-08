class Solution:
    def putMarbles( self, weights: List[int], k: int ) -> int:
        if k == 1:
            return 0
        
        sp = []
        
        for i in range( len( weights ) - 1 ):
            sp.append( weights[i] + weights[i + 1] )
            
        sp.sort()
            
        return sum( sp[1 - k:] ) - sum( sp[:k - 1] )