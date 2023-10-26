class Solution:
    
    def decodeString( self, s: str ) -> str:
        
        a = []
        
        for ch in s:
            if ch == "]":
                t = ""
                
                while a[-1] != "[":
                    t = a.pop() + t
                    
                a.pop()
                i = ""
                
                while len( a ) > 0 and a[-1].isdecimal():
                    i = a.pop() + i
                
                a.append( t * int( i ) )
            else:
                a.append( ch )
                
        return "".join( a )
