from collections import defaultdict

def prime_factors( n ):
    d = defaultdict( int )
    ans = ""
    
    while n > 1:
        for i in range( 2, n + 1):
            if n % i == 0:
                n //= i
                d[i] += 1
                break
                
    for i in sorted( d ):
        if d[i] > 1:
            ans += f"({i}**{d[i]})"
        else:
            ans += f"({i})"
            
    return ans
