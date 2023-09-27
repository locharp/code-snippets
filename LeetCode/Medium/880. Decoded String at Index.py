class Solution:
    def decodeAtIndex( self, s: str, k: int ) -> str:
        n = 0
        i = -1
        
        while n < k:
            i += 1
            
            if s[i].isdecimal():
                n *= int( s[i] )
            else:
                n += 1
                
                
                
        while i >= 0:
            if s[i].isalpha():
                if n == k or k == 0:
                    return s[i]
                
                n -= 1
            else:
                n //= int( s[i] )
                k %= n
                
                
            i -= 1
