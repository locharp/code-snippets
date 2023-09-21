class Solution:
    def getRow( self, rowIndex: int ) -> List[int]:
        d = [ [ 1 ], [ 1, 1 ] ]
        
        for i in range( 1, rowIndex ):
            row = [ 1 ]
            
            for j in range( i ):
                row.append( d[i][j] + d[i][ j + 1 ] )
                
            d.append( row + [ 1 ] )
            
        return d[ rowIndex ]