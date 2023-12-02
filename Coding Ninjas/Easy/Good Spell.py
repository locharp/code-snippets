def goodSpell( n: int, s: str ) -> int:
    
    p = q = 1
    
    for i in s[ : n // 2 ]:
        p *= int( i )

    for i in s[ n // 2 : ]:
        q *= int( i )

    return 1 if p == q else 0
