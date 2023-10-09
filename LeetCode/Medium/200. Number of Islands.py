class Solution:
    def numIslands( self, grid: List[ List[str] ] ) -> int:
        k = 0
        d = ( ( -1, 0 ), ( 0, -1 ), ( 1, 0 ), ( 0, 1 ) )
        q = deque()
        
        for i in range( len( grid ) ):
            for j in range( len( grid[0] ) ):
                if grid[i][j] == "1":
                    k += 1
                    grid[i][j] = k
                    q.append( ( i, j ) )
                    
                while len( q ) > 0:
                    m, n = q.pop()
                    
                    for r, s in d:
                        u, v = m + r, n + s
                        
                        if u >= 0 and u < len( grid ) and v >= 0 and v < len( grid[0] ) and grid[u][v] == "1":
                            grid[u][v] = k
                            q.append( ( u, v ) )
                            
        return k
