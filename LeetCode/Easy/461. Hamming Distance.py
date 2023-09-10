class Solution:
    def hammingDistance( self, x: int, y: int ) -> int:
        if y > x:
            x, y = y, x
            
        x = bin( x )
        y = bin( y )
        n = -len( y ) + 2
        
        return len( [ i for i in range( n, 0 ) if x[i] != y[i] ] ) + len( [ i for i in x[ : n ] if i == "1" ] )