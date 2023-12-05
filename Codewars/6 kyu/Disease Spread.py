def epidemic( tm, n, s0, i0, b, a ):
    
    dt = tm / n
    ans = 0
    
    for i in range( n ):
        i = b * s0 * i0 * dt
        r = a * i0 * dt
        s0 -= i
        i0 += i - r
        ans = max( ans, i0 )
        
    return int( ans )
