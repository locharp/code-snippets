class DSU:
    def __init__( self, n ):
        self.root = list( range( n ) )
        self.size = [ 1 ] * n
        
    def find( self, n ):
        if self.root[n] != n:
            self.root[n] = self.find( self.root[n] )
        
        return self.root[n]
    
    def union( self, m, n ):
        root_m = self.find( m )
        root_n = self.find( n )
        
        if root_m == root_n :
            return
        
        if self.size[root_m] > self.size[root_n]:
            self.root[root_n] = root_m
        elif self.size[root_m] < self.size[root_n]:
            self.root[root_m] = root_n
        else:
            self.root[root_n] = root_m
            self.size[m] += 1
            
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len( isConnected )
        dsu = DSU( n )
        ans = set()
        
        for i in range( n - 1 ):
            for j in range( i + 1, n ):
                if isConnected[i][j] == 1:
                    dsu.union( i, j )
        
        for i in range( n ):
            ans.add( dsu.find( i ) )
            
        return len( ans )