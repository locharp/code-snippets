def minOperations( x: int, a: int, b: list ) -> int:
    
    c = b - a
    
    return -1 if c < 1 or x % c != 0 else x // c
