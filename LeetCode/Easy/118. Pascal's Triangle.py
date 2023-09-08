class Solution:
    def generate( self, numRows: int ) -> List[List[int]]:
        ans = [ [ 1 ], [ 1, 1 ] ]
        
        if numRows < 3:
            return ans[ : numRows ]
        
        for i in range( 2, numRows ):
            row = [ 1 ]
            
            for j in range( 1, i ):
                row.append( ans[ i - 1 ][j] + ans[ i - 1 ][ j - 1 ] )
                
            ans.append( row + [ 1 ] )
            
        return ans