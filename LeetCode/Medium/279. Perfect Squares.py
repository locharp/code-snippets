class Solution:
    
    def numSquares( self, n: int ) -> int:
        
        d = { i * i for i in range( floor( sqrt( n ) ), 0, -1 ) }
        e = set()

        
        
        def f( a, c ):
            
            if n in a:
                return c
            
            e.update(a)

            return f( { i + j for i in a for j in d if i + j <= n and i + j not in e }, c + 1 )
                
                
                
        return f( { i for i in d }, 1 )
