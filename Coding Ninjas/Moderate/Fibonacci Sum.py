def fiboSum( n, m ):
    p, q = 0, 1
    ans = 1 if n < 2 else 0
    
    for i in range( 2, n ):
        p, q = q, p + q
        
    for i in range( max( n, 2 ), m + 1 ):
        p, q = q, p + q
        ans += q
        
    return ans % 1000000007
