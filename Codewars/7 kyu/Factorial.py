# Without limits
def factorial( n ):
    
    if n < 2:
        return 1
         
    return n * factorial( n - 1 )
  


# With limits
def factorial( n ):
    
    if n < 0 or n > 12:
        raise ValueError
    elif n < 2:
        return 1
         
    return n * factorial( n - 1 ) 
