class Solution:
    def __init__( self ):
        self.a = [ [], [ "()" ] ]
        
    def generateParenthesis( self, n: int ) -> List[str]:
        if n < len( self.a ):
            return self.a[n]
        
        self.generateParenthesis( n - 1 )
        self.a.append( set() )
        
        for i in range( 1, n // 2 + 1 ):
            for p in self.a[i]:
                for q in self.a[ n - i ]:
                    self.a[n].add( p + q )
                    self.a[n].add( q + p )
            
        for p in self.a[ n - 1 ]:
            self.a[n].add( "(" + p + ")" )
            
        return self.a[n]
