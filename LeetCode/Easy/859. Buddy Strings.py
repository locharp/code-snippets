class Solution:
    def buddyStrings( self, s: str, goal: str ) -> bool:
        m = len( s )
        n = len( goal )
        
        if m != n:
            return False
        
        if s == goal:
            return m != len( set( s ) )
        
        d1 = ""
        d2 = ""
        for ch1, ch2 in zip( s, goal ):
            if ch1 != ch2:
                if d1 != d2:
                    if d1 != ch2 or ch1 != d2:
                        return False
                    d1 = d2
                elif d1 == "":
                    d1 = ch1
                    d2 = ch2
                else:
                    return False
        
        return d1 == d2