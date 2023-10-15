class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        n = len( nums )
        s = sorted( ( j, i ) for i, j in enumerate( nums ) )
        
        for i in range( len( nums ) - indexDifference ):
            p = bisect_right( s, ( nums[i] - valueDifference, inf ) )
            q = bisect_left( s, ( nums[i] + valueDifference, 0 ) )
            
            if i + indexDifference > q - p:
                for j in range( i + indexDifference, n ):
                    if abs( nums[i] - nums[j] ) >= valueDifference:
                        return ( i, j )
            else:
                for j in range( p - 1, -1, -1 ):
                    if abs( i - s[j][1] ) >= indexDifference:
                        return ( i, s[j][1] )
                for j in range( q, n ):
                    if abs( i - s[j][1] ) >= indexDifference:
                        return ( i, s[j][1] )

        return ( -1, -1 )
