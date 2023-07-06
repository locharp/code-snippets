class DSU:
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
            return
        
        if self.sizes[root_x] > self.sizes[root_y]:
            self.roots[root_y] = root_x
        elif self.sizes[root_x] < self.sizes[root_y]:
            self.roots[root_x] = root_y
        else:
            self.roots[root_y] = root_x
            self.sizes[root_x] += 1
            
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len( s )
        dsu = DSU( n )
        
        for x, y in pairs:
            dsu.union( x, y )
        
        d = {}
        
        for i in range( n ):
            j = dsu.find( i )
            if j not in d:
                d[j] = [ [], [] ]
            d[j][0].append( i )
            d[j][1].append( s[i] )
            
        ns = [ "" ] * n
        
        for e in d.values():
            print(e)
            e[1].sort()
            
            for i in range( len( e[0] ) ):
                ns[e[0][i]] = e[1][i]
                
        return "".join( ns )