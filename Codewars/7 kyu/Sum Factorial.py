from functools import cache

@cache
def factorial( n ):
    
    if n < 2:
        return 1
         
    return n * factorial( n - 1 )



def sum_factorial( lst ):
    
    return sum( factorial( i ) for i in lst ) 
