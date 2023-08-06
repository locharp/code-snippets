class Solution:
    def isValidSudoku( self, board: List[List[str]] ) -> bool:
        board = [ [ 0 if n == "." else int( n ) for n in m ] for m in board ]
        
        for i in range( 3 ):
            for j in range( 3 ):
                t = [ [ False ] * 10 for _ in range( 3 ) ]
                u = i * 3 + j
                for m in range( 3 ):
                    for n in range( 3 ):
                        v = m * 3 + n
                        f = board[u][v]
                        g = board[v][u]
                        h = board[ i * 3 + m ][ j * 3 + n ]
                        
                        if f != 0 and t[0][f] or g != 0 and t[1][g] or h != 0 and t[2][h]:
                            return False
                            
                        t[0][f] = t[1][g] = t[2][h] = True
                        
        return True