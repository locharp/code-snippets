def simpleString( s: str ) -> int:
    
    n = len( s )
    s = list( s )
    ans = 0

    for i in range( 1, n ):
        if s[i] == s[ i - 1 ]:
            s[i] = "A"
            ans += 1

    return ans
