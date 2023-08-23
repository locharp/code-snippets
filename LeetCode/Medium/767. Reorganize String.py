class Solution:
    def reorganizeString( self, s: str ) -> str:
        n = len( s )
        d = dict( sorted( Counter( s ).items(), key = lambda c: c[1], reverse = True ) )
        c = list( d.keys() )
        
        if d[ c[0] ] > ( n + 1) // 2:
            return ""
        
        s = ""
        
        while len( c ) > 1 and d[ c[0] ] > d[ c[1] ]:
            s += c[0] + c[-1]
            d[ c[0] ] -= 1
            
            if d[ c[-1] ] == 1:
                c.pop()
            else:
                d[ c[-1] ] -= 1
            
        while len( c ) > 0:
            i = 0
            
            while i < len( c ):
                s += c[i]
                
                if d[ c[i] ] == 1:
                    c.pop( i )
                else:
                    d[ c[i] ] -= 1
                    i += 1
        
        return s
