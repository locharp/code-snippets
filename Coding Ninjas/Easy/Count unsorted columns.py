def countColumns( strings ):
    n = len( strings )
    m = len( strings[0] )
    ans = 0
    
    for i in range( m ):
        for j in range( 1, n ):
            if strings[ j - 1 ][i] > strings[j][i]:
               ans += 1
               break
                
    return ans
