def countPalindromeSubstrings( s: str ):
    n = len( s )
    ans = 0

    for i in range( n ):
        for j in range( i + 1, n + 1 ):
            if s[ i : j ] == s[ i : j ][ : : -1 ]:
                ans += 1

    return ans
