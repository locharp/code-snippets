class Solution:
    def winnerOfGame( self, colors: str ) -> bool:
        d = { "A": 0, "B": 0 }
        count = 1
        
        for i in range( 1, len( colors ) ):
            if colors[i] == colors[ i - 1 ]:
                count += 1
            else:
                d[ colors[ i - 1 ] ] += max( count - 2, 0 )
                count = 1
                
        d[ colors[-1] ] += max( count - 2, 0 )
        
        return d["A"] > d["B"]
