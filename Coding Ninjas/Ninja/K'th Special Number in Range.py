def kthSpecialNumber( l: int, r: int, k: int ) -> int:
    
    for i in range( l, r + 1):
        if "101" in bin( i ):
            k -= 1
            
            if k < 1:
                return i
        
    return -1
