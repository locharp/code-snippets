def checkSequence( a: int, d: int, x: int ) -> int:
    
    if d == 0:
        return 1 if a == x else 0

    return 1 if ( x - a ) % d == 0 else 0
