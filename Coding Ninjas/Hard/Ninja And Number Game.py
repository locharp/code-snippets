from math import gcd

def numbers( arr ):
    
    MOD = 10 ** 9 + 7
    p = arr[0] * arr[1]
    q = gcd( arr[0], arr[1] )

    for i in arr[ 2 : ]:
        p = ( p * i ) % MOD
        q = gcd( q, i )

    return int( pow( p, q, MOD ) )
