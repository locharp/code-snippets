def get_real_floor( n ):
    
    if n > 13:
        n -= 2
    elif n > 0:
        n -= 1
        
    return n
