class Solution:
    def maximalNetworkRank( self, n: int, roads: List[List[int]] ) -> int:
        a = [ set() for _ in range( n ) ]
        
        for road in roads:
            a[road[0]].add( road[1] )
            a[road[1]].add( road[0] )
            
        return max( len( a[i] ) + len( a[j] ) - ( 1 if i in a[j] else 0 ) for i in range( n - 1 ) for j in range( i + 1, n ) )