from math import floor

def is_square( n ): 
    if n < 0:
        return False
    
    return floor( pow( n, 0.5 ) ) == pow( n, 0.5 )
