from functools import lru_cache

@lru_cache( maxsize = 10000 )
def fibonacciNumber( n ):
    
    if n < 3:
        return 1
    
    return ( fibonacciNumber( n - 2 ) + fibonacciNumber( n - 1 ) ) % 1000000007
