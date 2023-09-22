class Solution:
    def searchMatrix( self, matrix: List[ List[int] ], target: int ) -> bool:
        q = len( matrix )
        
        if q < 1:
            return False
        
        s = len( matrix[0] )
        
        if s < 1:
            return False
        
        u = q // 2
        v = s // 2
        
        if matrix[u][v] == target:
            return True
        elif matrix[u][v] > target:
            if u > 0:
                if matrix[ u - 1 ][v] == target:
                    return True
                elif matrix[ u - 1 ][v] > target:
                    return self.searchMatrix( [ matrix[i][ : v ] for i in range( q ) ], target ) or self.searchMatrix( [ matrix[i][ v : ] for i in range( u - 1 ) ], target )
                else:
                    return self.searchMatrix( [ matrix[i][ v + 1 : ] for i in range( u ) ], target ) or self.searchMatrix( [ matrix[i][ : v ] for i in range( u, q ) ], target )
            else:
                return self.searchMatrix( [ matrix[u][ : v ] ], target )
        elif q > 2:
            if matrix[ u + 1 ][v] == target:
                return True
            if matrix[ u + 1 ][v] > target:
                return self.searchMatrix( [ matrix[i][ : v ] for i in range( u + 1, q ) ], target ) or self.searchMatrix( [ matrix[i][ v + 1 : ] for i in range( u + 1 ) ], target )
            else:
                return self.searchMatrix( [ matrix[i][ : v + 1 ] for i in range( u + 1, q ) ], target ) or self.searchMatrix( [ matrix[i][ v + 1 : ] for i in range( q ) ], target )
        else:
            return self.searchMatrix( [ matrix[u][ v + 1 : ] ], target )
