class Solution:
    def shortestBeautifulSubstring( self, s: str, k: int ) -> str:
        
        c = i = 0
        
        while i < len( s ) and s[i] == "0":
            i += 1
                
        j = i
        
        while j < len( s ) and c < k:
            if s[j] == "1":
                c += 1
            
            j += 1
            
        if c < k:
            return ""
        elif k == 1:
            return s[ i : j ]
        
        ans = int( s[ i : j ], 2 )
        i += 1
        
        while s[i] == "0":
            i += 1
        
        while j < len( s ):
            if s[j] == "1":
                ans = min( ans, int( s[ i : j + 1 ], 2 ) )
                i += 1
                
                while s[i] == "0":
                    i += 1
                    
            j += 1
            
        return bin( ans )[ 2 : ]
