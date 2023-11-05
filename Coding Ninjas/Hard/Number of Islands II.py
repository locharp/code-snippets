class DSU:
    
    def __init__( self, n, m ):

        self.roots = [ [ [ i, j ] for j in range( m ) ] for i in range( n ) ]
        self.sizes = [ [ 1 ] * m for i in range( n ) ]
        self.count = 0


    def find( self, n ):
        
        if self.roots[ n[0] ][ n[1] ] != n:
            self.roots[ n[0] ][ n[1] ] = self.find( self.roots[ n[0] ][ n[1] ] )

        return self.roots[ n[0] ][ n[1] ]
        
        

    def union( self, n, m ):
        root_n = self.find( [ n[0], n[1] ] )
        root_m = self.find( [ m[0], m[1] ] )
        
        if root_n == root_m:
            return

        if self.sizes[ root_n[0] ][ root_n[1] ] < self.sizes[ root_m[0] ][ root_m[1] ]:
            self.roots[ root_m[0] ][ root_m[1] ] = root_n
            self.sizes[ root_n[0] ][ root_n[1] ] += self.sizes[ root_m[0] ][ root_m[1] ]
        else:
            self.roots[ root_n[0] ][ root_n[1] ] = root_m
            self.sizes[ root_m[0] ][ root_m[1] ] += self.sizes[ root_n[0] ][ root_n[1] ]

        self.count -= 1

        return self.count

        


        
def numOfIslandsII( n, m, q ):
    
    dsu = DSU( n, m )
    dr = [ [ 1, 0 ], [ 0, 1 ], [ -1, 0 ], [ 0, -1 ] ]
    a = [ [ 0 ] * m for i in range( n ) ]
    ans = []
    
    for i, j in q:
        if a[i][j] == 0:
            a[i][j] = 1
            dsu.count += 1

            for o in dr:
                p = i + o[0]
                q = j + o[1]

                if p < 0 or p >= n or q < 0 or q >= m:
                    continue
                elif a[p][q] == 1:
                    dsu.union( [ i, j ], [ p, q ] )

            ans.append( dsu.count )

    return ans
