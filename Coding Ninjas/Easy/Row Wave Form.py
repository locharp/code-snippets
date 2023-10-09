def rowWaveForm( mat ):
    ans = []
    
    for i in range( len( mat ) ):
        if i % 2 < 1:
            ans += mat[i]
        else:
            ans += mat[i][ : : -1 ]
            
    return ans
