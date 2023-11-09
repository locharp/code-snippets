def array_divisibilty( n: int, x: List[int], y: List[int] ) -> int:
    
    ans = 0

    for i in range( n ):
        z = x[i] % y[i]
        ans += min( z, y[i] - z )

    return ans
