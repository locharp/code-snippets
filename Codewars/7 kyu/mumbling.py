def accum( s ):
    ans = ""
    
    for i in range( len( s ) ):
        ans += ( s[i] * ( i + 1 ) ).title() + "-"
        
    return ans[ : -1 ]