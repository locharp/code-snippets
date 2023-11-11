def stringReduction( s: str ) -> int:
    
    ans = 0
    
    for i in range( 1, len( s ) ):
        if s[i] == s[ i - 1 ]:
            ans += 1
            
    return ans
