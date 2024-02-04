from functools import cache

@cache
def fibonacciNumber( n: int ) -> int:
    
    if n < 2:
        return n
    
    return fibonacciNumber( n - 2 ) + fibonacciNumber( n - 1 )
