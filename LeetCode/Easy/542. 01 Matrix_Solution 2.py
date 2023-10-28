class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        d = ( ( 1, 0 ), ( 0, 1 ), ( -1, 0 ), ( 0, -1 ) )
        k = 10 ** 9
        m = len( mat )
        n = len( mat[0] )
        a = set()
        
        for i in range( m ):
            for j in range( n ):
                if mat[i][j] == 0:
                    a.add( ( i, j ) )
                else:
                    mat[i][j] = k
                    
                            
        for o in range( 1, k ):
            t = set()
            
            while len( a ) > 0:
                i, j = a.pop()
                
                for p, q in d:
                    r, s = i + p, j + q

                    if r >= 0 and r < len( mat) and s >= 0 and s < len( mat[0] ) and mat[r][s] == k:
                        mat[r][s] = o
                        t.add( ( r, s ) )
                        
            if len( t ) > 0:
                a = t
            else:
                break
                
        return mat
