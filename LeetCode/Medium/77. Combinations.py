class Solution:
    def combine( self, n: int, k: int ) -> List[ List[int] ]:
        
        def f( n, k, a, c ):
            if len( c ) == k + 1:
                a.append( c[ 1 : ] )
                return
            
            for i in range( c[-1] + 1, n - k + len( c ) + 1 ):
                c.append( i )
                f( n, k, a, c )
                c.pop()
                
            return a


        
        return f( n, k, [], [ 0 ] )
