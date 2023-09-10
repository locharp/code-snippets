class Solution:
    def romanToInt( self, s: str ) -> int:
        ans = 0
        d = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M' : 1000 }
        i = len( s ) - 1
        
        while i >= 0:
            m = d[ s[i] ]
            n = 0
            j = i - 1
            
            while j >= 0:
                if d[ s[j] ] < m:
                    n += d[ s[j] ]
                    i = j
                    j -= 1
                else:
                    break
                    
            ans += m - n
            i -= 1
            
        return ans