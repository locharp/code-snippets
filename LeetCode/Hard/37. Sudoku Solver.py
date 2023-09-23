class Solution:
    def solveSudoku( self, board: List[ List[str] ] ) -> None:
        
        def is_valid( x, y, z, board ):
            for i in range( 9 ):
                if board[i][y] == z or board[x][i] == z:
                    return False
            
            u = x // 3 * 3
            v = y // 3 * 3
            
            for i in range( 3 ):
                for j in range( 3 ):
                    if board[ u + i ][ v + j ] == z:
                        return False
                    
            return True
        
        
        
        def fill( x, y, board ):
            if x > 8:
                return True
            
            u = x if y < 8 else x + 1
            v = y + 1 if y < 8 else 0
            
            if board[x][y] == ".":
                for z in "123456789":
                    if is_valid( x, y, z, board ):
                        board[x][y] = z
                        
                        if fill( u, v, board ):
                            return True
                            
                        board[x][y] = "."
            else:        
                if fill( u, v, board ):
                    return True
                    
                        
                        
        fill( 0, 0, board )
