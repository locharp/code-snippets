def b_from_a( a: str, b: str ) -> int:
    
    c = Counter( a )
    d = Counter( b )
    ans = 10 ** 6

    for i, j in d.items():
        if i not in c:
            return 0
        
        ans = min( ans, c[i] // j )

    return ans
