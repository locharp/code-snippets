from string import ascii_lowercase

def makeStringsEqual( n: int, a: int, b: int, s: str, t: str ) -> int:
    
    A = ord( "a" )
    Z = ord( "z" )
    d = {}
    ans = 0

    for i in ascii_lowercase:
        d[i] = {}
        p = ord( i )

        for j in ascii_lowercase:
            q = ord( j )
            d[i][j] = min( abs( q - p ),
             p - A + b + Z - q, Z - p + a + q - A )

    for i in range( n ):
        ans += d[ s[i] ][ t[i] ]

    return ans
