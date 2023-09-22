class Solution:
    def isSubsequence( self, s: str, t: str ) -> bool:
        n = len( t )
        
        if n < len( s ):
            return False
        
        i = 0
        
        for ch in s:
            u = False
            
            while i < n:
                if t[i] == ch:
                    u = True
                    
                i += 1
                
                if u:
                    break
                    
            if not u:
                return u
            
        return True
