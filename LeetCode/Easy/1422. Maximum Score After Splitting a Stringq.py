class Solution:
    
    def maxScore( self, s: str ) -> int:
        
        c = s[ 1 : -1 ].count( "1" )
        
        if s[0] == "0":
            c += 1
            
        if s[-1] == "1":
            c += 1
            
        ans = c
        
        for i in s[ 1 : -1 ]:
            if i == "0":
                c += 1
                ans = max( ans, c )
            else:
                c -= 1
                
        return ans
