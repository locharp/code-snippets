class Solution:

    def destCity( self, paths: List[ List[str] ] ) -> str:
        
        d = defaultdict( int )

        for i, j in paths:
            d[i] += 1
            
            if j not in d:
                d[j] = 0

        for i, j in d.items():
            if j < 1:
                return i
