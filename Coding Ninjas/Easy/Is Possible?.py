from functools import lru_cache

@lru_cache( None )
def isPossible( a, b, c, d ):
    if a > c or b > d:
        return False
    elif a == c and b == d:
        return True
    else:
        return isPossible( a + b, b, c, d ) or isPossible( a, a + b, c, d )
