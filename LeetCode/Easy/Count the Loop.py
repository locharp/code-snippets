def countLoop( p: str, q: str ) -> int:
    
    p = int( p, 2 )
    q = int( q, 2 )
    ans = 0
    
    while q > 0:
        a = p & q
        p = p ^ q
        q = a * 2
        ans += 1

    return ans
