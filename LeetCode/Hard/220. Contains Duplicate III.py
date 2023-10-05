class Solution:
    def containsNearbyAlmostDuplicate( self, nums: List[int], indexDiff: int, valueDiff: int ) -> bool:
        n = len( nums )
        a = sorted( ( j, i ) for i, j in enumerate( nums ) )
        
        for i in range( n - 1 ):
            j = i + 1
            
            while j < n and a[j][0] - a[i][0] <= valueDiff:
                if abs( a[j][1] - a[i][1] ) <= indexDiff:
                    return True
                
                j += 1
                
        return False
