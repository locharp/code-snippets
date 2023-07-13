class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s ) == 0:
            return 0
        
        negative = False
        num = 0
        
        if s[0] == "+" or s[0] == "-":
            negative = s[0] == "-"
            s = s[1:]
        
        for ch in s:
            if not ch.isdecimal():
                break
                
            num = num * 10 + int( ch )
            
        if negative:
            num = -min( num, 2 ** 31 )
        else:
            num = min( num, 2 ** 31 - 1 )
        
        return num