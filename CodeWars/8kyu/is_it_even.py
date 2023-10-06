from math import floor

def is_even( n ): 
    if n != floor( n ):
        return False
    
    return n % 2 == 0
