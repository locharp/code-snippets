class Solution:
    
    def minimumSteps( self, s: str ) -> int:
        
        a = []
        
        for i in range( len( s ) ):
            if s[i] == "0":
                a.append( i )
            
        if len( a ) < 1:
            return 0
        else:
            return sum( a ) - sum( range( len( a ) ) )
