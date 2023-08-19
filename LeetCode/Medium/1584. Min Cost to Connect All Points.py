class union_find:
    def __init__( self, n ):
        self.roots = list( range( n ) )
        self.sizes = [ 1 ] * n
        
    def find( self, x ):
        if self.roots[x] != x:
            self.roots[x] = self.find( self.roots[x] )
            
        return self.roots[x]
    
    def union( self, x, y ):
        root_x = self.find( x )
        root_y = self.find( y )
        
        if root_x == root_y:
            return False
        
        if self.sizes[root_x] < self.sizes[root_y]:
            self.roots[root_x] = self.roots[root_y]
            self.sizes[root_y] += self.sizes[root_x]
        else:
            self.roots[root_y] = self.roots[root_x]
            self.sizes[root_x] += self.sizes[root_y]
            
        return True
    
class Solution:
    def minCostConnectPoints( self, points: List[List[int]] ) -> int:
        n = len( points )
        costs = []
        
        for i in range( n - 1 ):
            for j in range( i + 1, n ):
                costs.append( ( abs( points[i][0] - points[j][0] ) + abs( points[i][1] - points[j][1] ), i, j ) )
                
        costs.sort()
        uf = union_find( n )
        
        return sum( v for v, i, j in costs if uf.union( i, j ) )