from typing import List

def calculateNumberOfDays( s: str ) -> int:

    ans = i = 0
    
    while i < len( s ):
        if s[i] == "1":
            ans += 1
            i += 1
            
        i += 1
        
    return ans
